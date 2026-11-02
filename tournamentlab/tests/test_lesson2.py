import unittest

from lesson2 import calculate_average


class TestCalculateAverage(unittest.TestCase):

    def test_average_of_multiple_scores(self):
        self.assertEqual(
            calculate_average([10, 20, 30]),
            20.0
        )

    def test_average_of_one_score(self):
        self.assertEqual(
            calculate_average([15]),
            15.0
        )

    def test_empty_list_returns_none(self):
        self.assertIsNone(calculate_average([]))

    def test_negative_score_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_average([10, -5, 20])

    def test_decimal_score_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_average([10, 2.5, 20])

    def test_string_score_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_average([10, "20", 30])

    def test_boolean_score_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_average([10, True, 30])

    def test_non_list_input_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_average("10,20,30")


if __name__ == "__main__":
    unittest.main()