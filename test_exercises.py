import unittest

from validate_pin import validate_pin
from valid_parentheses import valid_parentheses


class ParenthesesTests(unittest.TestCase):
    def test_balanced_and_unbalanced_inputs(self) -> None:
        self.assertTrue(valid_parentheses("(())((()())())"))
        self.assertTrue(valid_parentheses(""))
        self.assertFalse(valid_parentheses(")(()))"))
        self.assertFalse(valid_parentheses("(()"))


class PinTests(unittest.TestCase):
    def test_only_four_or_six_ascii_digits_are_valid(self) -> None:
        self.assertTrue(validate_pin("1234"))
        self.assertTrue(validate_pin("123456"))
        self.assertFalse(validate_pin("12345"))
        self.assertFalse(validate_pin("a234"))


if __name__ == "__main__":
    unittest.main()
