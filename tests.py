import unittest

from helpers import get_dangerous_coords, \
    get_empty_coords, \
    get_flattened_list, \
    get_next_move, \
    get_snake_by_id


class TestHelperFuncs(unittest.TestCase):

    def test_get_dangerous_coords_no_snakes(self):
        # Arrange
        width = 3
        height = 3
        snake_coords = []
        expected = [
            [0, -1],
            [1, -1],
            [2, -1],
            [0, 3],
            [1, 3],
            [2, 3],
            [-1, 0],
            [-1, 1],
            [-1, 2],
            [3, 0],
            [3, 1],
            [3, 2],
        ]

        # Act
        dangerous_coords = get_dangerous_coords(width, height, snake_coords)

        # Assert
        self.assertEqual(sorted(expected), sorted(dangerous_coords))

    def test_get_dangerous_coords_one_snake(self):
        # Arrange
        width = 3
        height = 3
        snake_coords = [[1, 1]]
        expected = [
            [0, -1],
            [1, -1],
            [2, -1],
            [0, 3],
            [1, 3],
            [2, 3],
            [-1, 0],
            [-1, 1],
            [-1, 2],
            [3, 0],
            [3, 1],
            [3, 2],
            # Snake
            [1, 1],
        ]
        # Act
        dangerous_coords = get_dangerous_coords(width, height, snake_coords)

        # Assert
        self.assertEqual(sorted(expected), sorted(dangerous_coords))

    def test_get_empty_coords(self):
        # Arrange
        width = 3
        height = 3
        dangerous = [[0, 0], [0, 1], [0, 2], [2, 0], [2, 1], [2, 2], [1, 2]]
        expected = [[1, 0], [1, 1]]

        # Act
        empty_spaces = get_empty_coords(width, height, dangerous)

        # Assert
        self.assertEqual(sorted(expected), sorted(empty_spaces))

    def test_get_flattened_list(self):
        # Arrange
        snake_coords = [[[0, 1], [0, 2]], [[0, 3], [0, 4]], [[1, 1]]]
        expected = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 1]]

        # Act
        snake_coordinates = get_flattened_list(snake_coords)

        # Assert
        self.assertEqual(expected, snake_coordinates)

    def test_get_coords_for_id(self):
        # Arrange
        snake_id = "aaa"
        snakes = [
            {
                "id": snake_id,
                "coords": [[0, 1], [1, 1]]
            },
            {
                "id": "bbb",
                "coords": [[2, 1], [3, 1]]
            },
        ]
        expected = snakes[0]

        # Act
        snake = get_snake_by_id(snakes, snake_id)

        # Assert
        self.assertEqual(expected, snake)


if __name__ == '__main__':
    unittest.main()
