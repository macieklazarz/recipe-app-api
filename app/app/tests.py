from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_numbers(self):
        res = calc.add(5, 6)

        self.assertEquals(res, 11)

    def test_substract_numbers(self):

        res = calc.substract(10, 15)

        self.assertEqual(res, 5)
