#!/usr/bin/env python3
"""Place whole video tiles on matching color, feathering empty margins only.

Requires ffmpeg/ffprobe, Pillow and NumPy. Does no foreground chroma extraction.
Seat coordinates are pixel centres; rotations are 0/180 degrees, never mirrors.
"""
from pathlib import Path
import argparse
import json
import subprocess

import numpy as np
from PIL import Image


def pair(value):
    return tuple(int(v) for v in value.lower().split('x'))


def frame(pipe, size):
    result = bytearray()
    while len(result) < size:
        block = pipe.read(size-len(result))
        if not block:
            return None
        result.extend(block)
    return bytes(result)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('input', type=Path)
    ap.add_argument('output', type=Path)
    ap.add_argument('--canvas', type=pair, required=True)
    ap.add_argument('--tile', type=pair, required=True)
    ap.add_argument('--seat', action='append', required=True, help='centre_x,centre_y,0_or_180')
    ap.add_argument('--background', required=True, help='RGB matched to the selected source background')
    ap.add_argument('--inset', type=int, default=0, help='Verified empty padding to fade out fully before feathering')
    ap.add_argument('--feather', type=int, default=32)
    ap.add_argument('--margin-color-tolerance', type=int, default=45)
    ap.add_argument('--fps', type=int, default=24)
    ap.add_argument('--seconds', type=float, required=True)
    ap.add_argument('--receipt', type=Path)
    a = ap.parse_args()
    seats = [tuple(int(v) for v in s.split(',')) for s in a.seat]
    color = tuple(int(v) for v in a.background.split(','))
    tw, th = a.tile
    if len(color)!=3 or any(v<0 or v>255 for v in color):
        ap.error('Background must be three RGB bytes')
    if (min(*a.canvas,tw,th,a.fps,a.seconds)<=0 or a.inset<0 or a.feather<0
            or a.inset+a.feather>=min(tw,th)/2 or (a.inset and not a.feather)):
        ap.error('Invalid dimensions, duration, fps or feather')
    if any(len(s)!=3 or s[2] not in (0,180) for s in seats):
        ap.error('Seats need x,y,0 or x,y,180')
    count = round(a.seconds*a.fps)
    if abs(count/a.fps-a.seconds)>1e-6:
        ap.error('Duration must be a whole number of frames')
    if a.output.exists() or (a.receipt and a.receipt.exists()):
        ap.error('Output or receipt already exists; use a new run path')
    rects = [(x-tw//2,y-th//2,x-tw//2+tw,y-th//2+th) for x,y,_ in seats]
    for i,r in enumerate(rects):
        for s in rects[:i]:
            if min(r[2],s[2])>max(r[0],s[0]) and min(r[3],s[3])>max(r[1],s[1]):
                ap.error('Whole tiles overlap; choose separate placement or a scoped occlusion mask')
    info = json.loads(subprocess.check_output([
        'ffprobe','-v','error','-show_streams','-of','json',str(a.input)]))
    stream = next(s for s in info['streams'] if s['codec_type']=='video')
    w,h = stream['width'],stream['height']
    yy,xx = np.indices((th,tw))
    distance = np.minimum.reduce([xx,yy,tw-1-xx,th-1-yy])
    t = np.clip((distance-a.inset)/max(a.feather,1),0,1) if a.feather else np.ones((th,tw))
    edge = Image.fromarray(np.rint((t*t*(3-2*t))*255).astype(np.uint8))
    margin = distance<a.inset+a.feather
    decoder = subprocess.Popen([
        'ffmpeg','-v','error','-i',str(a.input),'-vf','fps=%d'%a.fps,
        '-frames:v',str(count),'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
    encoder = subprocess.Popen([
        'ffmpeg','-v','error','-n','-f','rawvideo','-pix_fmt','rgb24',
        '-s','%dx%d'%a.canvas,'-r',str(a.fps),'-i','-','-an',
        '-c:v','libx264','-crf','16','-preset','fast','-pix_fmt','yuv420p',
        '-movflags','+faststart',str(a.output)],stdin=subprocess.PIPE)
    completed = 0
    peak_margin_difference = 0
    error = None
    try:
        for i in range(count):
            data = frame(decoder.stdout,w*h*3)
            if data is None:
                raise RuntimeError('Source ended before requested frame count')
            tile = Image.frombytes('RGB',(w,h),data).resize((tw,th),Image.Resampling.LANCZOS)
            if a.feather:
                diff = int(np.max(np.abs(np.asarray(tile,dtype=np.int16)[margin]-np.asarray(color))))
                peak_margin_difference = max(diff,peak_margin_difference)
                if diff>a.margin_color_tolerance:
                    raise RuntimeError('Frame%d: feather margin contains mismatched color or foreground; reduce feather or clean only that region'%i)
            canvas = Image.new('RGB',a.canvas,color)
            for (x,y,angle),r in zip(seats,rects):
                rotated = tile.transpose(Image.Transpose.ROTATE_180) if angle else tile
                alpha = edge.transpose(Image.Transpose.ROTATE_180) if angle else edge
                canvas.paste(rotated,(r[0],r[1]),alpha)
            encoder.stdin.write(canvas.tobytes())
            completed += 1
    except Exception as exc:
        error = exc
    finally:
        decoder.stdout.close();encoder.stdin.close()
        if error:
            decoder.terminate()
        exits = [decoder.wait(),encoder.wait()]
    if error:
        raise error
    if completed!=count or any(exits):
        raise RuntimeError('Incomplete encode: %d, exits%s'%(completed,exits))
    result = {'method':'Whole tiles; matching-color canvas; smoothstep feather on verified empty margins; no chroma extraction',
              'frames':completed,'fps':a.fps,'seconds':a.seconds,'canvas':a.canvas,'tile':a.tile,
              'seats':seats,'background_rgb':color,'empty_inset_px':a.inset,'feather_px':a.feather,
              'peak_margin_color_difference':peak_margin_difference,'mirrored':False,
              'projection_calibrated':False}
    if a.receipt:
        with a.receipt.open('x') as f:
            json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result))


if __name__=='__main__':
    main()
