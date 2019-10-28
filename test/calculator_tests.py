import unittest

from calculator import Calculator

class CalculatorTests(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(10, 20), 30)
    
    def test_subtract(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(10, 20), -10)

    def test_multiply(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(10, 20), 20)

    def test_divide(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(10, 20), 0.5)

def suite():
    """
    Test suite
    :return: The test suite
    """
    suite = unittest.TestSuite()

    suite.addTests(
       unittest.TestLoader().loadTestsFromTestCase(CalculatorTests)
    )
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())