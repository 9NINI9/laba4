import unittest
from Circle import area
from Circle import perimeter


class MyTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5), 78.53981633974483)

    def test_perimeter(self):
        self.assertEqual(perimeter(7), 43.982297150257104)


if __name__ == '__main__':
    unittest.main()
