def get_dangerous_coords(width, height, flattened_snake_coords):
    """Returns a list of all dangerous coordinates"""
    # All edges are dangerous
    danger_coords = []
    for x in range(width):
        # Top and bottom walls
        danger_coords.append([x, -1])
        danger_coords.append([x, height])
    for y in range(height):
        # Left wall and right walls
        danger_coords.append([-1, y])
        danger_coords.append([width, y])

    # Return edges plus currently occupied snakes
    return danger_coords + flattened_snake_coords


def get_empty_coords(width, height, dangerous_coords):
    """Returns a list of all empty coordinates in the game board"""
    # All possible board coordinates minus dangerous coords (ie walls and snakes)
    all_board_coordinates = [[x, y] for x in range(width) for y in range(height)]
    return [coord for coord in all_board_coordinates if coord not in dangerous_coords]


def get_flattened_list(list_of_lists):
    """Returns a flattened list from a list of lists"""
    return [snake_coord for coords in list_of_lists for snake_coord in coords]


def get_snake_by_id(snakes, snake_id):
    snake = None
    for curr_snake in snakes:
        if curr_snake['id'] == snake_id:
            snake = curr_snake
            break
    return snake


def get_direction_from_coord(coord, curr_position):
    next_x, next_y = coord
    curr_x, curr_y = curr_position
    move = ""

    if next_x < curr_x:
        move = "left"
    elif next_x > curr_x:
        move = "right"
    elif next_y > curr_y:
        move = "down"
    else:
        move = "up"

    return move


def get_next_move(snake, empty_coords, food_coords):
    health = snake['health']
    curr_x, curr_y = snake['coords'][0]
    adjacent_coords = [
        [curr_x + 1, curr_y],
        [curr_x - 1, curr_y],
        [curr_x, curr_y + 1],
        [curr_x, curr_y - 1],
    ]
    # Get all coords that are adjacent and empty
    possible_move_coords = [coord for coord in adjacent_coords if coord in empty_coords]

    # TODO check if hungry then go for food

    next_coord = None
    # For now just take the first one
    if possible_move_coords:
        next_coord = possible_move_coords[0]

    return get_direction_from_coord(next_coord, [curr_x, curr_y])
