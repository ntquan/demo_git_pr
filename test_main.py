import unittest
from unittest.mock import patch
from main import calculate_sum_and_average, get_numbers_from_user

class TestCalculateFunctions(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertEqual(calculate_sum_and_average([1, 2, 3]), (6, 2.0))

    def test_empty_list(self):
        with self.assertRaises(ValueError) as context:
            calculate_sum_and_average([])
        self.assertEqual(str(context.exception), "Dãy số không được rỗng nha.")

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average([1, -2, 3])

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average(["a", "b", "c"])

    def test_get_numbers_from_user_valid(self):
        # This test is not practical to run automatically since it requires user input.
        # Instead, we can mock the input function to simulate user input.
        with patch('builtins.input', return_value='1 2 3 4'):
            numbers = get_numbers_from_user()
            self.assertEqual(numbers, [1, 2, 3, 4])

    def test_valid_numbers_2(self):
        self.assertEqual(calculate_sum_and_average([1, 2, 4]), (7, 2.3333333333333335))

if __name__ == '__main__':
    unittest.main()
