import unittest

from triangle import area
from triangle import perimeter

class MyTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5, 6), 15)

    def test_perimetr(self):
        self.assertEqual(perimeter(5, 6, 7), 18)

if __name__ == '__main__':
    unittest.main()
