import unittest
from objects import Point, Circle


class TestCases(unittest.TestCase):
    def test_point(self):
        # Testing point, a class that manages a point in R2
        point = Point(3, 4)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 4)

        self.assertTrue(point == Point(3, 4))
        self.assertFalse(point == Point(4, 3))

        self.assertEqual(str(point), '(3, 4)')

        self.assertEqual(point.distance(Point(0, 0)), 5)
        self.assertAlmostEqual(point.distance(Point(4, 3)), 2 ** 0.5, 3)

    def test_circle(self):
        # Testing circle, a class that manages circles in R2
        circle = Circle(Point(3, 4), 5)
        unit_circle = Circle(Point(0, 0), 1)
        circle1 = Circle(Point(-1, -1), 2 ** 0.5)
        circle2 = Circle(Point(-1, -1), 1)

        self.assertEqual(circle.radius, 5)
        self.assertEqual(circle.center, Point(3, 4))
        self.assertEqual(circle.center.x, 3)
        self.assertEqual(circle.center.y, 4)

        self.assertTrue(circle == Circle(Point(3, 4), 5))
        self.assertFalse(circle == Circle(Point(4, 3), 5))
        self.assertFalse(circle == Circle(Point(3, 4), 1))

        self.assertFalse(circle != Circle(Point(3, 4), 5))
        self.assertTrue(circle != Circle(Point(4, 3), 5))
        self.assertTrue(circle != Circle(Point(3, 4), 1))

        self.assertEqual(str(circle), '5 @ (3, 4)')

        self.assertTrue(circle.overlaps(unit_circle))
        self.assertTrue(circle.overlaps(circle1))
        self.assertFalse(circle.overlaps(circle2))


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
