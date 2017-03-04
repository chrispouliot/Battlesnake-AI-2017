def get_dangerous_coords(width, length, snake_coords):
    # All edges are dangerous
    danger_coords = []
    for x in range(width):
        danger_coords.append([x, 0])
        danger_coords.append([x, length - 1])
    for y in range(1, length - 1):
        danger_coords.append([0, y])
        danger_coords.append([width - 1, y])

    # Return edges plus currently occupied snakes
    return danger_coords + snake_coords


def get_safe_coords():
    pass
