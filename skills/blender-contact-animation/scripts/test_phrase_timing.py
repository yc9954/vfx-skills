"""Timeline math tests only; not choreography or production-rig validation."""
import unittest
from phrase_timing import schedule, boundary_frame


def plan(beats=None, phrases=None, fps=30):
    return {'fps': fps, 'beat_times_seconds': beats if beats is not None else [0, .5, 1],
            'phrases': phrases if phrases is not None else
            [{'id': 'first', 'beat_start': 0, 'beat_end': 1},
             {'id': 'second', 'beat_start': 1, 'beat_end': 2}]}


class PhraseTimingTests(unittest.TestCase):
    def test_decimal_half_frame_boundaries(self):
        for seconds, fps, expected in [(1.025, 60, 62), (.145, 100, 15), (.125, 100, 13)]:
            with self.subTest(seconds=seconds, fps=fps):
                self.assertEqual(boundary_frame(seconds, fps), expected)
                result = schedule(plan([0, seconds], [{'id':'one','beat_start':0,'beat_end':1}], fps))
                self.assertEqual(result['end_frame_exclusive'], expected + 1)

    def test_near_half_is_not_snapped(self):
        self.assertEqual(boundary_frame(1.02499999999, 60), 61)
        self.assertEqual(boundary_frame(1.02500000001, 60), 62)

    def test_half_open_boundaries_no_overlap(self):
        result = schedule(plan())
        self.assertEqual(result['frame_count'], 30)
        self.assertEqual(result['first_frame'], 1)
        self.assertEqual(result['end_frame_exclusive'], 31)
        self.assertEqual(result['phrases'][0]['end_frame_exclusive'], result['phrases'][1]['start_frame'])

    def test_variable_tempo_and_audio_offset(self):
        result = schedule(plan(beats=[2, 2.4, 3.1]))
        self.assertEqual(result['first_frame'], 61)
        self.assertEqual([p['frame_count'] for p in result['phrases']], [12, 21])

    def test_rounding_does_not_accumulate(self):
        beats = [i * 60 / 123 for i in range(401)]
        phrases = [{'id': str(i), 'beat_start': i, 'beat_end': i+1} for i in range(400)]
        result = schedule(plan(beats, phrases, fps=29.97))
        self.assertEqual(result['frame_count'], int(beats[-1] * 29.97 + .5))
        for row in result['phrases']:
            self.assertLessEqual(abs(row['end_rounding_error_seconds']), .5/29.97 + 1e-10)

    def test_bad_markers(self):
        for beats in [[0, 0, 1], [0, -1, 2], [0, float('nan'), 1], [0, float('inf'), 2], [0, True, 2]]:
            with self.subTest(beats=beats), self.assertRaises(ValueError):
                schedule(plan(beats=beats))

    def test_invalid_fps(self):
        for fps in [0, -30, float('inf'), True]:
            with self.subTest(fps=fps), self.assertRaises(ValueError):
                schedule(plan(fps=fps))

    def test_gaps_overlaps_and_duplicate_ids(self):
        for start in [0, 2]:
            candidate = plan()
            candidate['phrases'][1]['beat_start'] = start
            with self.assertRaises(ValueError):
                schedule(candidate)
        candidate = plan()
        candidate['phrases'][1]['id'] = 'first'
        with self.assertRaises(ValueError):
            schedule(candidate)

    def test_full_span_required(self):
        with self.assertRaises(ValueError):
            schedule(plan(phrases=[{'id': 'partial', 'beat_start': 0, 'beat_end': 1}]))

    def test_subframe_phrase_rejected(self):
        with self.assertRaises(ValueError):
            schedule(plan(beats=[0, .0001, 1]))

    def test_no_motion_claim_and_preserves_direction(self):
        candidate = plan()
        candidate['phrases'][0]['intent'] = 'deliberate sideways step'
        result = schedule(candidate)
        self.assertEqual(result['scope'], 'timing_only_not_motion_or_audio_validation')
        self.assertEqual(result['phrases'][0]['intent'], candidate['phrases'][0]['intent'])
        self.assertIn('contact', result['excluded'])


if __name__ == '__main__':
    unittest.main()
