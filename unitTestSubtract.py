import unittest
import simpleCalculator

class SubtractTests(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testSub1(self):
        self.assertEqual(simpleCalculator.subtract(10, 3), 7)

    def testSub2(self):
        self.assertEqual(simpleCalculator.subtract(11, 90), -79)

    def testSub3(self):
        self.assertEqual(simpleCalculator.subtract(1, 25), -24)


if __name__ == '__main__':
    unittest.main()