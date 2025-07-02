import unittest

import constants


class TestConstantsFunctions(unittest.TestCase):
    def test_given_true_then_vline_is_red(self):
        self.assertEqual(constants.get_vline_colour(True), 8)

    def test_given_false_then_vline_is_black(self):
        self.assertEqual(constants.get_vline_colour(False), 0)

    def test_single_char_then_pixel_width_is_ten(self):
        self.assertEqual(constants._width_of_string_in_pixels(1), 10)

    def test_two_chars_then_pixel_width_is_22(self):
        self.assertEqual(constants._width_of_string_in_pixels(2), 22)

    def test_given_empty_string_then_exception_thrown(self):
        self.assertRaises(ValueError, lambda: constants.text_centre_x(""))

    def test_given_single_char_string_then_centre_is_505(self):
        self.assertEqual(constants.text_centre_x("A"), 505)

    def test_given_two_char_string_then_centre_is_499(self):
        self.assertEqual(constants.text_centre_x("AA"), 499)


if __name__ == "__main__":
    unittest.main()
