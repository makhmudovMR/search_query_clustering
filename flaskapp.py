from flask import Flask, request, redirect
from flask import render_template
from config import *

import sqlite3

app = Flask(__name__)

'''<----views---->'''

@app.route('/')
def index():
    return render_template('index.html', name=None)

@app.route('/page1')
def page1():
    return render_template('page2.html')


'''<------handlers------>'''
@app.route('/handler1', methods=['POST'])
def handler1():
    f = open('db.txt', 'a', encoding='utf-8')
    f.write(str(request.form['search']) + '\n')
    f.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)