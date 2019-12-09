"""CIS 189
Alex Rickels
Final Project - Unit Tests"""


import unittest
from files.ord_class import *


class OrderTest(unittest.TestCase):

    def setUp(self):
        self.ord = Order('2', ['carbonara', 'spaghetti', 'focaccia'])

    def tearDown(self):
        del self.ord

    # def test_something(self):
    #     self.assertEqual(, False)

    def test__blank_table(self):
        with self.assertRaises(EnterTableNumber):
            ord = Order('', ['carbonara', 'spaghetti', 'focaccia'])

    def test__invalid_table_input(self):
        with self.assertRaises(InvalidTableNumber):
            ord = Order('five', ['carbonara', 'spaghetti', 'focaccia'])

    def test__table_out_of_range(self):
        with self.assertRaises(InvalidTableNumber):
            ord = Order('18', ['carbonara', 'spaghetti', 'focaccia'])

    def test_non_menu_lasagna(self):
        with self.assertRaises(InvalidDishError):
            ord = Order('4', ['carbonara', 'spaghetti', 'lasagna'])

    def test_blank_dishes(self):
        with self.assertRaises(MissingOrderError):
            ord = Order('4', [])


if __name__ == '__main__':
    unittest.main()
