# unittest for objects

import unittest
from nested_list import groups_of_3, final_value, repeat_value


class TestCases(unittest.TestCase):
    def test_groups_of_3(self):
        # Testing groups_of_3, which turns list
        # into 2D list with 3 element sublists
        self.assertListEqual(groups_of_3([1, 2, 3, 4, 5, 6, 7, 8, 9]),
                             [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        self.assertListEqual(groups_of_3([1, 2, 3, 4, 5, 6, 7, 8]),
                             [[1, 2, 3], [4, 5, 6], [7, 8]])

        self.assertListEqual(groups_of_3([1, 2, 3, 3, 2]), [[1, 2, 3], [3, 2]])

    def test_final_value(self):
        # Testing final_value, which gets list
        # of final values from each sublist
        self.assertListEqual(final_value([[-1, 12, 3], [8], [], [1, -3]]),
                             [3, 8, -3])

        self.assertListEqual(final_value([[1, 5, 12], [-142, -2, -431]]),
                             [12, -431])

        self.assertListEqual(final_value([[], [], []]), [])

    def test_repeat_value(self):
        # Testing repeat_value, which extends 2D list to 3D
        self.assertListEqual(repeat_value([1, 3, 0]), [[1], [3, 3, 3], []])
        self.assertListEqual(repeat_value([1, 1, 1]), [[1], [1], [1]])
        self.assertListEqual(repeat_value([1, 5, 3, 0]),
                             [[1], [5, 5, 5, 5, 5], [3, 3, 3], []])


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
