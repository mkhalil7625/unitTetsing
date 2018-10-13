import unittest
import simpleCalculator

class AdditionTests(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testAdd1(self):
        self.assertEqual(simpleCalculator.add(10, 3), 13)

    def testAdd2(self):
        self.assertEqual(simpleCalculator.add(11, 90), 101)

    def testAdd3(self):
        self.assertEqual(simpleCalculator.add(1, 25), 26)


if __name__ == '__main__':
    unittest.main()