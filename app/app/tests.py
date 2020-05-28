from django.test import TestCase

from app.calc import add, subtract

class CalcTests(TestCase):

    def test_add_number(self):
        """Test the two number are added"""
        self.assertEqual(add(3,8), 11)

    def test_subtract_number(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(5,11),6)