import logging
import os
from flask import Flask, json, request
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
    }
    return json.dumps(response_dict)


@app.route('/move', methods=["POST"])
def handle_move():
    request_dict = request.get_json()
    # Sanity check
    if not request_dict:
        return 400

    response_dict = "Placeholder"
    return json.dumps(response_dict)


if __name__ == '__main__':
    logging.info("Starting server..")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
