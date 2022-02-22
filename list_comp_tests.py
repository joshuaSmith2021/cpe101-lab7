# list comprehension tests
import unittest
from list_comp import point_distance_all, are_in_first_quadrant, \
                      circle_distance_all, overlaps_all

from objects import Circle, Point


class TestCases(unittest.TestCase):
    def test_point_distance_all(self):
        # Testing point_distance_all, which returns a list representing the
        # distance of each point from origin.
        p1 = Point(3, 4)  # 5
        p2 = Point(9, 40)  # 41
        p3 = Point(15, 112)  # 113
        self.assertListEqual(point_distance_all([p1, p2, p3]), [5, 41, 113])

        p4 = Point(20, 21)  # 29
        p5 = Point(24, 143)  # 145
        p6 = Point(28, 195)  # 197
        self.assertListEqual(point_distance_all([p4, p5, p6]), [29, 145, 197])

        p7 = Point(33, 56)  # 65
        p8 = Point(36, 323)  # 325
        self.assertListEqual(point_distance_all([p7, p8]), [65, 325])

    def test_are_in_first_quadrant(self):
        # Testing are_in_first_quadrant, which filter out points that are not
        # in the first quadrant.
        points1 = list(map(lambda x: Point(*x), [(-4, 2), (-421, 24), (0, 0),
                                                 (4, 2), (2, 6)]))

        correct1 = [x for i, x in enumerate(points1) if i in [3, 4]]
        self.assertListEqual(are_in_first_quadrant(points1), correct1)

        points2 = list(map(lambda x: Point(*x), [(4, 2), (5, 2), (-2, 0)]))
        correct2 = [x for i, x in enumerate(points2) if i in [0, 1]]
        self.assertListEqual(are_in_first_quadrant(points2), correct2)

        points3 = list(map(lambda x: Point(*x), [(0, 0), (6, 6), (6, -5)]))
        correct3 = [x for i, x in enumerate(points3) if i == 1]
        self.assertListEqual(are_in_first_quadrant(points3), correct3)

    def test_circle_distance_all(self):
        # Testing circle_distance_all, which returns center of each circle
        # from the origin.
        data1 = [(0, 0, 5), (3, 4, 10), (9, 40, 2)]
        circles1 = [Circle(Point(*x[:2]), x[2]) for x in data1]
        self.assertListEqual(circle_distance_all(circles1), [0, 5, 41])

        data2 = [(15, 112, 4), (20, 21, -4), (24, 143, 0.01)]
        circles2 = [Circle(Point(*x[:2]), x[2]) for x in data2]
        self.assertListEqual(circle_distance_all(circles2), [113, 29, 145])

        data3 = [(28, 195, 2), (33, 56, 29), (36, 323, 1)]
        circles3 = [Circle(Point(*x[:2]), x[2]) for x in data3]
        self.assertListEqual(circle_distance_all(circles3), [197, 65, 325])

    def test_overlaps_all(self):
        # Testing overlaps_all, which returns which circles overlap with the
        # unit circle.
        data1 = [(0, 0, 5), (3, 4, 10), (9, 40, 2)]
        circles1 = [Circle(Point(*x[:2]), x[2]) for x in data1]
        correct1 = [x for i, x in enumerate(circles1) if i in [0, 1]]
        self.assertListEqual(overlaps_all(circles1), correct1)

        data2 = [(15, 112, 4), (20, 21, -4), (24, 143, 144.1)]
        circles2 = [Circle(Point(*x[:2]), x[2]) for x in data2]
        correct2 = [x for i, x in enumerate(circles2) if i == 2]
        self.assertListEqual(overlaps_all(circles2), correct2)

        data3 = [(28, 195, 197), (33, 56, 65.1), (36, 323, 324)]
        circles3 = [Circle(Point(*x[:2]), x[2]) for x in data3]
        correct3 = [x for i, x in enumerate(circles3) if i in [0, 1]]
        self.assertListEqual(overlaps_all(circles3), correct3)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
