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
    formatter = logging.Formatter("{%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = logging.StreamHandler()
    handler.setLevel(logging.ERROR)
    handler.setFormatter(formatter)

    app.logger.addHandler(handler)

    logging.getLogger('flask_cors').level = logging.INFO

    app.run()
