import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
       # result = calc.add(10, 5)
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
       # result = calc.add(10, 5)
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
       # result = calc.add(10, 5)
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divided(self):
       # result = calc.add(10, 5)
        self.assertEqual(calc.divided(10, 5), 2)
        self.assertEqual(calc.divided(-1, 1), -1)
        self.assertEqual(calc.divided(-1, -1), 1)
        self.assertEqual(calc.divided(5, 2), 2.5)

        #self.assertRaises(ValueError, calc.divided, 10, 2)
        # using context manager
        with self.assertRaise(ValueError):
            calc.divided(10, 0)



if __name__ == '__main__':
    unittest.main()
