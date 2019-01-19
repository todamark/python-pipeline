import unittest
from Pipeline import Pipeline


class TestPipeline(unittest.TestCase):
    def test_straight_one_step(self):
        pipe = Pipeline()
        pipe = pipe.pipe(lambda x: x + [1])
        self.assertEqual(pipe.apply([]), [1])

    def test_straight_multi_step(self):
        pipe = Pipeline()
        pipe = pipe.pipe(lambda x: x + [1])
        pipe = pipe.pipe(lambda x: x + [5])
        pipe = pipe.pipe(lambda x: x + [17])
        self.assertEqual(pipe.apply([]), [1, 5, 17])

    def test_straight_inline_one_step(self):
        res = Pipeline().pipe(lambda x: x + [1]).apply([])
        self.assertEqual(res, [1])

    def test_straight_inline_multi_step(self):
        res = Pipeline().pipe(lambda x: x + [1]).pipe(lambda x: x + [5]).pipe(lambda x: x + [17]).apply([])
        self.assertEqual(res, [1, 5, 17])

    def test_split(self):
        pipe = Pipeline()
        pipe = pipe.split(lambda x: x > 1, 1, 0)
        self.assertEqual(pipe.apply(5), 1)
        self.assertEqual(pipe.apply(-10), 0)
