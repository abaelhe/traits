import unittest
from traits.util.camel_case import camel_case_to_python as camel_case_to_python, camel_case_to_words as camel_case_to_words

class CamelCaseTestCase(unittest.TestCase):
    def test_python_conversion(self) -> None: ...
    def test_word_conversion(self) -> None: ...
