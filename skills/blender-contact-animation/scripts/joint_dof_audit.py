"""Read-only, calibrated HINGE rotation audit; not a grasp/clinical validator.

Run with Blender's Python (or a Python environment providing bpy):
  python joint_dof_audit.py --scene candidate.blend --config hinge-map.json --out receipt.json
  blender -b --python joint_dof_audit.py -- --scene candidate.blend --config hinge-map.json --out receipt.json

Config example (synthetic limits, NOT human normative values):
{"armature":"Rig", "frames":{"start":1,"end":100,"step":0.5},
 "calibration_note":"Checked local X positive flexion in neutral and bent views",
 "joints":[{"bone":"Index_PIP.L", "kind":"hinge", "axis_local":[1,0,0],
            "flexion_deg":[0,90], "max_off_axis_deg":5}]}

axis_local is in that bone's REST frame. Establish it from anatomical observation,
not the same failing driver being tested. Off-axis swing includes all rotation not
around that axis. Multi-DOF joints (MCP, thumb CMC, wrist, hip, shoulder), coupled
knee kinematics and the ankle/foot complex are intentionally unsupported. A knee
declared as a simplified hinge is checked only as that rotational approximation;
this tool does not verify translations, balance, skin or anatomical validity.
Receipt covers only listed joints, sampled times, supplied calibration/limits.
Outputs are exclusive-create. The source blend is never saved or modified on disk.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys


def hinge_angles(quaternion, axis):
    from mathutils import Quaternion, Vector
    axis = Vector(axis)
    if not all(math.isfinite(x) for x in axis) or axis.length < 1e-8:
        raise ValueError('Zero hinge axis')
    axis.normalize()
    if not all(math.isfinite(x) for x in quaternion) or quaternion.magnitude < 1e-8:
        raise ValueError('Undefined evaluated rotation; cannot certify joint')
    q = quaternion.normalized()
    if not all(math.isfinite(x) for x in q):
        raise ValueError('Non-finite evaluated rotation; cannot certify joint')
    if q.w < 0:
        q.negate()
    projection = Vector((q.x, q.y, q.z)).dot(axis)
    norm = math.hypot(q.w, projection)
    if norm < 1e-8:
        # A 180-degree off-axis rotation has no unique hinge twist.
        return None, 180.0
    twist = Quaternion((q.w/norm, *(axis*(projection/norm))))
    swing = q @ twist.conjugated()
    angle = math.degrees(2*math.atan2(projection/norm, q.w/norm))
    angle = (angle+180) % 360-180
    return angle, math.degrees(2*math.acos(min(1.0, abs(swing.w))))


def require_invertible(matrix, label):
    """Reject collapsed/non-finite frames before quaternion extraction can hide them.

    The determinant is normalized by column lengths so valid miniature scale is
    not rejected merely for being small. Reflections are unsupported, not evidence
    of an anatomical defect; require a positively oriented calibrated frame.
    """
    if not all(math.isfinite(v) for row in matrix for v in row):
        raise ValueError(label + ': non-finite transform')
    basis = matrix.to_3x3()
    lengths = [basis.col[i].length for i in range(3)]
    if min(lengths) < 1e-12:
        raise ValueError(label + ': collapsed transform')
    normalized = basis.copy()
    for i in range(3):
        normalized.col[i] = basis.col[i] / lengths[i]
    if normalized.determinant() <= 1e-6:
        raise ValueError(label + ': singular or reflected transform is unsupported')


def relative_delta(pose_bone):
    rest = pose_bone.bone.matrix_local
    pose = pose_bone.matrix
    require_invertible(rest, 'rest')
    require_invertible(pose, 'pose')
    if pose_bone.parent:
        require_invertible(pose_bone.parent.bone.matrix_local, 'parent rest')
        require_invertible(pose_bone.parent.matrix, 'parent pose')
        rest = pose_bone.parent.bone.matrix_local.inverted() @ rest
        pose = pose_bone.parent.matrix.inverted() @ pose
    delta = rest.inverted() @ pose
    require_invertible(delta, 'rest-relative pose')
    return delta.to_quaternion().normalized()


def validate_config(config):
    if not config.get('calibration_note', '').strip():
        raise ValueError('Missing calibration_note; uncalibrated axes cannot pass')
    if not config.get('armature') or not config.get('joints'):
        raise ValueError('An armature and explicit joint mapping are required')
    seen = set()
    for j in config['joints']:
        if j.get('kind') != 'hinge':
            raise ValueError('Only calibrated hinge joints are supported')
        if j['bone'] in seen:
            raise ValueError('Duplicate bone mapping')
        seen.add(j['bone'])
        axis = j['axis_local']
        if len(axis) != 3 or not all(math.isfinite(x) for x in axis) or sum(x*x for x in axis)<1e-12:
            raise ValueError('Invalid hinge axis')
        lo, hi = j['flexion_deg']
        off = j['max_off_axis_deg']
        if not all(math.isfinite(x) for x in [lo,hi,off]) or not -180<=lo<hi<=180 or not 0<=off<180:
            raise ValueError('Invalid explicitly calibrated angular limits')
    spec = config['frames']
    if isinstance(spec, dict):
        start,end,step = spec['start'],spec['end'],spec['step']
        if not all(math.isfinite(x) for x in [start,end,step]) or step<=0 or end<start:
            raise ValueError('Invalid sample interval')
        count = math.floor((end-start)/step+1e-9)+1
        if count>20000:
            raise ValueError('More than 20000 samples; split the interval')
        frames = [start+i*step for i in range(count)]
        if frames[-1]<end-1e-9:frames.append(end)
    else:
        frames = list(spec)
    if not frames or len(frames)>20000 or not all(math.isfinite(x) for x in frames):
        raise ValueError('Invalid frames')
    return frames


def audit(scene, armature, config):
    import bpy
    frames = validate_config(config)
    for joint in config['joints']:
        if joint['bone'] not in armature.pose.bones:
            raise ValueError('Missing mapped bone: '+joint['bone'])
    rows=[]
    for frame in frames:
        whole=math.floor(frame)
        scene.frame_set(whole,subframe=frame-whole)
        evaluated=armature.evaluated_get(bpy.context.evaluated_depsgraph_get())
        for joint in config['joints']:
            pb=evaluated.pose.bones[joint['bone']]
            try:
                flex,off=hinge_angles(relative_delta(pb),joint['axis_local'])
            except ValueError as error:
                rows.append({'frame':frame,'bone':joint['bone'],'flexion_deg':None,
                             'off_axis_deg':None,'failures':['invalid_transform'],
                             'reason':str(error)})
                continue
            lo,hi=joint['flexion_deg']
            failures=[]
            if flex is None:failures.append('ambiguous_twist')
            elif not lo-1e-4<=flex<=hi+1e-4:failures.append('flexion_range')
            if off>joint['max_off_axis_deg']+1e-4:failures.append('off_axis_rotation')
            rows.append({'frame':frame,'bone':joint['bone'],'flexion_deg':flex,
                         'off_axis_deg':off,'failures':failures})
    failures=[r for r in rows if r['failures']]
    return {'verdict':'failed' if failures else 'verified_for_stated_hinge_scope',
            'scope':'Only mapped calibrated hinge DOF at sampled times; supplied limits are not independently certified.',
            'excluded':['thumb opposition','multi-axis joint biomechanics','coupled joint translations',
                        'whole-body balance','skin deformation','hand/prop support',
                        'between-sample collision','natural performance'],
            'config':config,'failed_samples':len(failures),'samples':rows}


def main():
    parser=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--scene',required=True,type=Path)
    parser.add_argument('--config',required=True,type=Path)
    parser.add_argument('--out',required=True,type=Path)
    args=parser.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else None)
    if args.out.exists():raise FileExistsError(args.out)
    config=json.loads(args.config.read_text());validate_config(config)
    import bpy
    bpy.ops.wm.open_mainfile(filepath=str(args.scene.resolve()))
    arm=bpy.data.objects.get(config['armature'])
    if arm is None or arm.type!='ARMATURE':raise ValueError('Mapped armature not found')
    result=audit(bpy.context.scene,arm,config)
    result['scene']=str(args.scene.resolve());result['scene_sha256']=hashlib.sha256(args.scene.read_bytes()).hexdigest()
    with args.out.open('x') as file:json.dump(result,file,indent=2)
    print(result['verdict'], 'failed joint samples:', result['failed_samples'])
    return int(result['failed_samples']>0)

if __name__=='__main__':sys.exit(main())
