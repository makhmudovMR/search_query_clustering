from flask import Flask
from flask import render_template
from config import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', name=None)

if __name__ == '__main__':
    app.run(debug=True)