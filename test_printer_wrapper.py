import unittest
from unittest.mock import patch

import printer_wrapper


class TestPrinterWrapper(unittest.TestCase):

    def test_given_document_name_then_calls_lp_d_with_document_name(self):
        filename = "some-document.pdf"
        with patch("printer_wrapper.call") as mock_call:
            printer_wrapper.print_document(filename)
        mock_call.assert_called_once_with(["lp", "-d", "M834", filename])


if __name__ == "__main__":
    unittest.main()
