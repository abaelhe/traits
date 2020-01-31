import unittest
from traits.util.clean_strings import clean_filename as clean_filename
from typing import Any

LEGAL_CHARS: Any

class TestCleanStrings(unittest.TestCase):
    def test_clean_filename_default(self) -> None: ...
    def test_clean_filename_whitespace_handling(self) -> None: ...
    def test_clean_filename_conversion_to_lowercase(self) -> None: ...
    def test_clean_filename_accented_chars(self) -> None: ...
    def test_clean_filename_all_chars(self) -> None: ...
    def check_output(self, safe_string: Any) -> None: ...