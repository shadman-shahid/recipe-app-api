"""
sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """ Test the calc module."""
    def test_add_numbers(self):
        """ test the calc module."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting number"""

        res = calc.subtract(5, 6)
        self.assertEqual(res, 1)
