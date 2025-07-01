import unittest

import constants


class TestHelperFunctions(unittest.TestCase):
    def test_given_true_then_vline_is_red(self):
        self.assertEqual(constants.get_vline_colour(True), 8)

    def test_given_false_then_vline_is_black(self):
        self.assertEqual(constants.get_vline_colour(False), 0)

    def test_given_empty_string_then_pixel_length_is_zero(self):
        self.assertEqual(constants._width_of_string_in_pixels(""), 0)

    def test_single_char_then_pixel_length_is_ten(self):
        self.assertEqual(constants._width_of_string_in_pixels("A"), 10)


if __name__ == "__main__":
    unittest.main()
