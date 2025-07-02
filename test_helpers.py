import unittest

import helpers


class TestHelperFunctions(unittest.TestCase):

    def test_given_frame_22_then_returns_true(self):
        self.assertTrue(helpers.flash_text(30 + 22))

    def test_given_frame_29_then_returns_false(self):
        self.assertFalse(helpers.flash_text(30 + 29))


if __name__ == "__main__":
    unittest.main()
