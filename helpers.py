def get_adjacent_coords_for_coord(coord):
    x, y = coord
    return [
        [x, y + 1],
        [x, y - 1],
        [x + 1, y],
        [x - 1, y],
    ]


def get_all_board_coords(width, height):
    return [[x, y] for x in range(width) for y in range(height)]


def get_dangerous_coords(width, height, flattened_snake_coords, max_danger_level):
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

    # Add snake coords to list of danger
    danger_coords += flattened_snake_coords

    # Add empty spaces that are surrouned by dangerous coords to list of danger
    empty_coords = get_all_board_coords(width, height)
    for empty_coord in empty_coords:
        adjacent_coords = get_adjacent_coords_for_coord(empty_coord)
        num_dangerous = 0
        for adjacent_coord in adjacent_coords:
            if adjacent_coord in danger_coords:
                num_dangerous += 1
        # If empty space is surrounded by dangerous coords, it's dangerous
        if num_dangerous >= max_danger_level:
            danger_coords.append(empty_coord)

    # Return edges plus currently occupied snakes
    return danger_coords


def get_safe_coords(width, height, dangerous_coords):
    """Returns a list of all empty coordinates in the game board"""
    # All possible board coordinates minus dangerous coords (ie walls and snakes)
    all_board_coordinates = get_all_board_coords(width, height)
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


def get_next_move(snake, empty_coords, food_coords, min_health_level):
    health = snake['health_points']
    curr_coord = snake['coords'][0]
    adjacent_coords = get_adjacent_coords_for_coord(curr_coord)
    # Get all coords that are adjacent and empty
    possible_move_coords = [coord for coord in adjacent_coords if coord in empty_coords]

    next_coord = None

    # Super simple food retrieval
    if health < min_health_level:
        # Check if we're beside food
        for coord in possible_move_coords:
            if coord in food_coords:
                # Get that food
                next_coord = food_coords
                break
    else:
        # Wander safely
        # Placeholder
        import random
        next_coord = random.choice(possible_move_coords)

    return get_direction_from_coord(next_coord, curr_coord)
