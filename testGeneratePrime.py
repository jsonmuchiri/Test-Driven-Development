import unittest
from maincode.generatePrime import prime_number


class TestPrimeGenerator(unittest.TestCase):
    def test_is_working(self):
        """Testing if prime numbers are correctly generated."""

        self.assertEqual(prime_number(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_zero_not_prime(self):
        """Testing if zero is correctly determined not to be prime."""

        self.assertEqual(prime_number(0), "Zero or One cannot be prime numbers.")

    def test_one_not_prime(self):
        """"Testing if one is correctly determined not to be prime."""

        self.assertEqual(prime_number(1), "Zero or One cannot be prime numbers.")

    def test_two(self):
        """Testing if error returned if integer entered is 2."""

        self.assertEqual(prime_number(2), [2])

    def test_input_is_string(self):
        """Testing if error returned if input not integer."""

        self.assertEqual(prime_number("String"), "Only integers are allowed.")

    def test_input_not_integer(self):
        """Testing if error returned if input not integer."""

        self.assertEqual(prime_number(set()), "Only integers are allowed.")


if __name__ == "__main__":
    unittest.main()
