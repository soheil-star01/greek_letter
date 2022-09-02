import random

from flask import Flask

app = Flask(__name__)


# listening for a request and retrieving a random letter
@app.route('/letter')
def get_greek_letter():
    letters = ['\u0391', '\u0392', '\u0393', '\u0394', '\u0395', '\u0396', '\u0397', '\u0398', '\u0399',
               '\u039A', '\u039B', '\u039C', '\u039D', '\u039E', '\u039F', '\u03A0', '\u03A1', '\u03A3',
               '\u03A4', '\u03A5', '\u03A6', '\u03A7', '\u03A8', '\u03A9', '\u03B1', '\u03B2', '\u03B3',
               '\u03B4', '\u03B5', '\u03B6', '\u03B7', '\u03B8', '\u03B9', '\u03BA', '\u03BB', '\u03BC',
               '\u03BD', '\u03BE', '\u03BF', '\u03C0', '\u03C1', '\u03C2', '\u03C3', '\u03C4', '\u03C5',
               '\u03C6', '\u03C7', '\u03C8', '\u03C9', '\u03D1', '\u03D2', '\u03D6']

    # return random.choice(letters)
    return '\u0000'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
