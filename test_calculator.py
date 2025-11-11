# https://github.com/tyler-ufl/lab10-TW-MO
# Partner 1: Tyler Whittlesey
# Partner 2: Michelle Ocon

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ####### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 7), 9)
        self.assertEqual(add(4, 6), 10)
        self.assertEqual(add(3, 9), 12)
    # ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 7), 14)
        self.assertEqual(mul(-4, 6), -24)
        self.assertEqual(mul(-3, -9), 27)
    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(-3, 9), -3)
        self.assertEqual(div(-4, -16), 4)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10, 1), 0)
        self.assertEqual(logarithm(3, 81), 4)
        self.assertEqual(logarithm(10, 100), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    # ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(9, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(6, 4), 7.2111026)
        self.assertAlmostEqual(hypotenuse(5, 9), 10.2956301)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        # with self.assertRaises(ValueError):
        #     square_root(-2)
        self.assertEqual(square_root(-2), 'Error: math domain error')
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(81), 9)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
