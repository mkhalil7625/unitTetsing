import unittest
import simpleCalculator

class MultiblacationTests(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testMultiply1(self):
        self.assertEqual(simpleCalculator.multiply(10, 300), 3000)

    def testMultiply2(self):
        self.assertEqual(simpleCalculator.multiply(11, 90), 990)

    def testMultiply3(self):
        self.assertEqual(simpleCalculator.multiply(0, 25), 0)


if __name__ == '__main__':
    unittest.main()