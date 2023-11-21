import unittest
from rectangle import area
from rectangle import perimeter

class MyTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5, 6), 30)

    def test_perimetr(self):
        self.assertEqual(perimeter(2, 3), 10)


if __name__ == '__main__':
    unittest.main()
