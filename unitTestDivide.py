import unittest
import simpleCalculator

class DivisionTests(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testDivide1(self):
        self.assertEqual(simpleCalculator.divide(10, 5), 2)

    def testDivide2(self):
        self.assertEqual(simpleCalculator.divide(1000, 10), 100)

    def testDivide3(self):
        self.assertEqual(simpleCalculator.divide(0, 25), 0)


if __name__ == '__main__':
       unittest.main()