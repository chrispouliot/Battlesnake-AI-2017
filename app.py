import logging
from flask import Flask, json, request
app = Flask(__name__)


@app.route('/')
def handle_index():
    return "This isn't what you want"


@app.route('/start', methods=["POST"])
def handle_start():
    return json.dumps({"what": "hey"})


@app.route('/move', methods=["POST"])
def handle_move():
    pass


if __name__ == '__main__':
    app.run()
