import logging
from flask import Flask
app = Flask(__name__)


@app.route('/')
def handle_index():
    return "This isn't what you want"


@app.route('/start')
def handle_start():
    pass


@app.route('/move')
def handle_move():
    pass


if __name__ == 'main':
    app.run()
