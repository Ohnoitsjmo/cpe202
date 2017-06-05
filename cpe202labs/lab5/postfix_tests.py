import unittest
from postfix import *

class TestPostfix(unittest.TestCase):
    def test00_interface(self):
        postfix_calc("1 1 +")

    def test_add(self):
        self.assertEqual(postfix_calc("1 2 + 3 +"), 6.0)   
        self.assertEqual(postfix_calc("1 1 +"), 2.0)

    def test_subtract(self):
        self.assertEqual(postfix_calc("2 1 -"), 1.0)
        self.assertEqual(postfix_calc("5 1 - 1 -"), 3.0)
        self.assertEqual(postfix_calc("5.0 1.0 -"), 4.0)

    def test_multiply(self):
        self.assertEqual(postfix_calc("2 1 *"), 2)
        self.assertEqual(postfix_calc("2 1 * 3 *"), 6.0)

    def test_division(self):
        self.assertAlmostEqual(postfix_calc("2 1 /"), 2.0)
        self.assertAlmostEqual(postfix_calc("16 4 / 2 /"), 2.0)
        self.assertAlmostEqual(postfix_calc("7.0 2 1 / / 10 3 / / 0.5 /"), 2.1)

    def test_combo(self):
        self.assertAlmostEqual(postfix_calc("2 1 + 3 / 3 * 2 -"), 1.0)
        self.assertAlmostEqual(postfix_calc("2 3 4 5.0 6 + - * /"), -0.09523809)

if __name__ == "__main__":
    unittest.main()
