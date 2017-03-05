import logging
import os
from flask import Flask, json, request

from constants import COORD_DANGER_LEVEL_MAX, MIN_FOOD_HEALTH_LEVEL
from helpers import get_dangerous_coords, \
    get_safe_coords, \
    get_flattened_list, \
    get_next_move, \
    get_snake_by_id

app = Flask(__name__)


@app.route('/')
def handle_index():
    return "This isn't what you want"


@app.route('/start', methods=["POST"])
def handle_start():
    response_dict = {
        'color': '#ffb6c1',
        'name': 'pinky-snek',
        'head_type': 'safe',
        'head_url': 'https://s3.amazonaws.com/john-box-o-mysteries/pacman+ghosts/pinky.png',
        'tail_type': 'round-bum',
        'taunt': 'wakawakawakawaka',
    }
    return json.dumps(response_dict)


@app.route('/move', methods=["POST"])
def handle_move():
    request_dict = request.get_json()
    # Sanity check
    if not request_dict:
        return 400

    # Raw board data from request
    snake_id = request_dict['you']
    width = request_dict['width']
    height = request_dict['height']
    food_coords = request_dict['food']
    snakes = request_dict['snakes']

    # Inferred board data
    flattened_snake_coords = get_flattened_list([snake['coords'] for snake in snakes])
    our_snake = get_snake_by_id(snakes, snake_id)
    dangerous_coords = get_dangerous_coords(width, height, flattened_snake_coords, COORD_DANGER_LEVEL_MAX)
    safe_coords = get_safe_coords(width, height, dangerous_coords)

    # We're good
    return json.dumps({'move': get_next_move(our_snake, safe_coords, food_coords, MIN_FOOD_HEALTH_LEVEL)})


if __name__ == '__main__':
    # logging.info("Starting server..")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
