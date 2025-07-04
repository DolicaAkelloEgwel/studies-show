import unittest
from unittest.mock import patch

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

    def test_given_453_pixel_border_then_max_chars_per_line_is_10(self):
        text = "hello"
        with patch("constants.textwrap.wrap") as mock_wrap:
            constants.wrap_text_for_border(text, 453)
        mock_wrap.assert_called_once_with(text, 10)

    def test_centered_text(self):
        text = "hello"
        y = 8
        centered_text = constants.CenteredText(text, y)
        self.assertEqual(text, centered_text.text)
        self.assertEqual(y, centered_text.y)
        self.assertEqual(constants.text_centre_x(text), centered_text.x)


if __name__ == "__main__":
    unittest.main()
