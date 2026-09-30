"""Synthetic rotation/Blender invariance tests; not evidence for a character rig."""
import unittest,math
import bpy
from mathutils import Quaternion,Vector,Matrix
from types import SimpleNamespace
from joint_dof_audit import hinge_angles,relative_delta,validate_config,audit

class RotationTests(unittest.TestCase):
    def test_undefined_quaternion_rejected_before_normalization(self):
        with self.assertRaises(ValueError):hinge_angles(Quaternion((0,0,0,0)), (1,0,0))

    def test_collapsed_and_reflected_frames_cannot_pass(self):
        for scale in [(0,0,0), (1,0,1), (-1,1,1)]:
            pb=SimpleNamespace(parent=None,bone=SimpleNamespace(matrix_local=Matrix.Identity(4)),
                               matrix=Matrix.Diagonal((*scale,1)))
            with self.subTest(scale=scale), self.assertRaises(ValueError):relative_delta(pb)

    def test_small_positive_scale_keeps_rotation(self):
        pose=Quaternion((0,1,0),math.radians(60)).to_matrix().to_4x4() @ Matrix.Scale(1e-5,4)
        pb=SimpleNamespace(parent=None,bone=SimpleNamespace(matrix_local=Matrix.Identity(4)),matrix=pose)
        _,off=hinge_angles(relative_delta(pb),(1,0,0));self.assertGreater(off,59.9)

    def test_nonfinite_matrix_rejected(self):
        pose=Matrix.Identity(4);pose[0][3]=float('nan')
        pb=SimpleNamespace(parent=None,bone=SimpleNamespace(matrix_local=Matrix.Identity(4)),matrix=pose)
        with self.assertRaises(ValueError):relative_delta(pb)

    def test_full_audit_records_invalid_transform(self):
        bpy.ops.wm.read_factory_settings(use_empty=True);bpy.ops.object.armature_add();a=bpy.context.object
        bone=a.pose.bones[0];bone.scale=(0,0,0);a.update_tag()
        cfg={'armature':a.name,'calibration_note':'synthetic X', 'frames':[1],
             'joints':[{'bone':bone.name,'kind':'hinge','axis_local':[1,0,0],
                        'flexion_deg':[0,90],'max_off_axis_deg':5}]}
        result=audit(bpy.context.scene,a,cfg)
        self.assertEqual(result['verdict'],'failed')
        self.assertEqual(result['samples'][0]['failures'],['invalid_transform'])

    def test_signed_flexion(self):
        for a in [-35,0,45,90]:
            flex,off=hinge_angles(Quaternion(Vector((1,0,0)),math.radians(a)),(1,0,0))
            self.assertAlmostEqual(flex,a,places=4);self.assertLess(off,.06)
    def test_twisted_finger(self):
        flex,off=hinge_angles(Quaternion(Vector((0,1,0)),math.radians(60)),(1,0,0))
        self.assertAlmostEqual(flex,0,places=4);self.assertGreater(off,59.9)
    def test_mirrored_axis_and_quaternion_sign(self):
        q=Quaternion(Vector((1,0,0)),math.radians(35));q.negate()
        f,_=hinge_angles(q,(-1,0,0));self.assertAlmostEqual(f,-35,places=4)
    def test_singular_swing_is_not_pass(self):
        f,off=hinge_angles(Quaternion((0,0,1,0)),(1,0,0))
        self.assertIsNone(f);self.assertEqual(off,180)
    def test_no_calibration_or_mapping(self):
        for config in [{},{'calibration_note':'checked','armature':'X','joints':[]}]:
            with self.assertRaises(ValueError):validate_config(config)
    def test_parent_rotation_does_not_change_joint_measurement(self):
        import bpy
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.object.armature_add();a=bpy.context.object
        bpy.ops.object.mode_set(mode='EDIT');root=a.data.edit_bones[0];root.name='Parent'
        child=a.data.edit_bones.new('Hinge');child.head=(0,0,1);child.tail=(0,0,2);child.parent=root
        bpy.ops.object.mode_set(mode='OBJECT')
        p=a.pose.bones['Parent'];c=a.pose.bones['Hinge'];p.rotation_mode=c.rotation_mode='QUATERNION'
        c.rotation_quaternion=Quaternion(Vector((1,0,0)),math.radians(40))
        for angle in [0,45,120]:
            p.rotation_quaternion=Quaternion(Vector((0,1,0)),math.radians(angle));bpy.context.view_layer.update()
            f,off=hinge_angles(relative_delta(c),(1,0,0));self.assertAlmostEqual(f,40,places=3);self.assertLess(off,.06)
    def test_full_audit_rejects_twist_and_accepts_only_hinge_scope(self):
        bpy.ops.wm.read_factory_settings(use_empty=True);bpy.ops.object.armature_add();a=bpy.context.object
        bone=a.pose.bones[0];bone.rotation_mode='QUATERNION'
        cfg={'armature':a.name,'calibration_note':'Synthetic X hinge, not a human ROM claim',
             'frames':{'start':1,'end':2,'step':.5},'joints':[{'bone':bone.name,
             'kind':'hinge','axis_local':[1,0,0],'flexion_deg':[0,90],'max_off_axis_deg':5}]}
        bone.rotation_quaternion=Quaternion(Vector((0,1,0)),math.radians(60));a.update_tag()
        bad=audit(bpy.context.scene,a,cfg)
        self.assertEqual(bad['verdict'],'failed');self.assertEqual(bad['failed_samples'],3)
        bone.rotation_quaternion=Quaternion(Vector((1,0,0)),math.radians(45));a.update_tag()
        good=audit(bpy.context.scene,a,cfg)
        self.assertEqual(good['verdict'],'verified_for_stated_hinge_scope')
        self.assertIn('natural performance',good['excluded'])
    def test_multi_axis_and_coupled_joints_not_falsely_certified(self):
        cfg={'armature':'A','calibration_note':'test','frames':[1],
             'joints':[{'bone':'Joint','kind':'thumb_cmc','axis_local':[1,0,0],
                        'flexion_deg':[0,90],'max_off_axis_deg':5}]}
        for kind in ['thumb_cmc','ball_socket','coupled_knee','ankle_complex']:
            with self.subTest(kind=kind):
                cfg['joints'][0]['kind']=kind
                with self.assertRaises(ValueError):validate_config(cfg)

if __name__=='__main__':unittest.main()
