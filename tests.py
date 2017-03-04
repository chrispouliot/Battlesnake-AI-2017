import unittest

from helpers import get_dangerous_coords


class TestHelperFuncs(unittest.TestCase):

    def test_dangerous_coords_no_snakes(self):
        # Arrange
        width = 3
        length = 3
        snake_coords = []
        expected = [[0, 0], [0, 1], [0, 2], [1, 0], [2, 0], [2, 1], [2, 2], [1, 2]]
        # Act
        dangerous_coords = get_dangerous_coords(width, length, snake_coords)
        # raise Exception(dangerous_coords)

        # Assert
        self.assertEqual(sorted(expected), sorted(dangerous_coords))


if __name__ == '__main__':
    unittest.main()
