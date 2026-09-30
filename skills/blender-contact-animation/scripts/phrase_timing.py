"""Map supplied music/phrase markers to a drift-free half-open frame timeline.

This is a planning helper, NOT a beat detector, motion generator or quality audit.
Input JSON: fps, optional frame_start (default 1), beat_times_seconds (strictly
increasing, non-negative), phrases with unique id and beat_start/beat_end indices.
Phrases must cover the marker span contiguously. Extra phrase fields are retained.
Time zero maps to frame_start. Boundaries round individually (half upward), never
by accumulating rounded phrase lengths. end_frame_exclusive is NOT Blender's
inclusive scene.frame_end; subtract one when setting an inclusive render range.

python phrase_timing.py plan.json --out timeline.json
Without --out, print JSON. Output file is exclusive-create; no source is changed.
"""
import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def number(value, name):
    if isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value):
        raise ValueError(f'{name} must be a finite number')
    return value


def integer(value, name):
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f'{name} must be an integer')
    return value


def boundary_frame(seconds, fps):
    """Round the decimal spelling of nonnegative inputs half upward, exactly.

    Avoid float multiplication at half-frame boundaries (1.025 * 60). This does
    not guess an intended rational rate or snap genuinely sub-half boundaries.
    """
    value = Fraction(str(seconds)) * Fraction(str(fps))
    return (2 * value.numerator + value.denominator) // (2 * value.denominator)


def schedule(plan):
    fps = number(plan['fps'], 'fps')
    if not 0 < fps <= 1000:
        raise ValueError('fps must be in (0,1000]')
    origin = integer(plan.get('frame_start', 1), 'frame_start')
    if origin < 0:
        raise ValueError('frame_start must be non-negative')
    beats = plan['beat_times_seconds']
    if not isinstance(beats, list) or not 2 <= len(beats) <= 100000:
        raise ValueError('Provide 2..100000 beat markers including the ending boundary')
    for index, time in enumerate(beats):
        number(time, f'beat[{index}]')
        if time < 0 or (index and time <= beats[index - 1]):
            raise ValueError('Beat markers must be non-negative and strictly increasing')
    if not isinstance(plan['phrases'], list) or not plan['phrases']:
        raise ValueError('At least one phrase required')
    rows, seen, next_beat = [], set(), 0
    for phrase in plan['phrases']:
        name = phrase['id']
        if not isinstance(name, str) or not name.strip() or name in seen:
            raise ValueError('Phrase IDs must be nonempty, unique strings')
        seen.add(name)
        start = integer(phrase['beat_start'], 'beat_start')
        end = integer(phrase['beat_end'], 'beat_end')
        if start != next_beat or not 0 <= start < end < len(beats):
            raise ValueError('Phrases must be ordered, contiguous and within beat indices')
        first = origin + boundary_frame(beats[start], fps)
        stop = origin + boundary_frame(beats[end], fps)
        if stop <= first:
            raise ValueError('Phrase shorter than one sampled frame; revise timing/fps')
        rows.append({**phrase, 'start_seconds': beats[start], 'end_seconds': beats[end],
                     'start_frame': first, 'end_frame_exclusive': stop, 'frame_count': stop - first,
                     'start_rounding_error_seconds': (first - origin) / fps - beats[start],
                     'end_rounding_error_seconds': (stop - origin) / fps - beats[end]})
        next_beat = end
    if next_beat != len(beats) - 1:
        raise ValueError('Phrases must cover the final marker')
    return {'scope': 'timing_only_not_motion_or_audio_validation', 'fps': fps,
            'frame_start_at_time_zero': origin, 'interval_convention': '[start,end)',
            'first_frame': rows[0]['start_frame'], 'end_frame_exclusive': rows[-1]['end_frame_exclusive'],
            'frame_count': sum(row['frame_count'] for row in rows),
            'requested_span_seconds': beats[-1] - beats[0], 'phrases': rows,
            'excluded': ['beat detection', 'audio audition', 'actual generated frame count',
                         'musicality', 'animation continuity', 'contact', 'performance quality']}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('plan', type=Path)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    raw = args.plan.read_bytes()
    result = schedule(json.loads(raw))
    result['input'] = str(args.plan.resolve())
    result['input_sha256'] = hashlib.sha256(raw).hexdigest()
    payload = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + '\n'
    if args.out:
        with args.out.open('x') as stream:
            stream.write(payload)
    else:
        print(payload, end='')


if __name__ == '__main__':
    main()
