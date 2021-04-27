import unittest
import calculator_module

class Testing(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator_module.add(-1,-1),-2)
        self.assertEqual(calculator_module.add(10,5), 15)
        self.assertEqual(calculator_module.add(1,-1), 0)

    def test_subtraction(self):
        self.assertEqual(calculator_module.sub(-1, -1), 0)
        self.assertEqual(calculator_module.sub(10, 5), 5)
        self.assertEqual(calculator_module.sub(1, -1), 2)

    def test_multiplication(self):
        self.assertEqual(calculator_module.mul(-1, -1), 1)
        self.assertEqual(calculator_module.mul(10, 5), 50)
        self.assertEqual(calculator_module.mul(1, -1), -1)

if __name__ == '__main__':
    unittest.main()