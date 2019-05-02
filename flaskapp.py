from flask import Flask, request, redirect
from flask import render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from config import *

import sqlite3

app = Flask(__name__)

'''<----views---->'''

@app.route('/')
def index():
    return render_template('index.html', name=None)


@app.route('/table')
def table():
    # вытаскиваем данные
    f = open('db.txt', 'r', encoding='utf-8')
    data = f.read().split('\n')[:-1]
    print(data)
    text_data = data.copy()

    # разделяем на кластеры
    tf = TfidfVectorizer(min_df=2) # Объект с помощью которого мы проведём векторизацию
    
    data = tf.fit_transform(data)
    kmeans = KMeans(n_clusters=2, n_init=10, max_iter=300)
    kmeans.fit(data)

    alist = []
    for key, label in zip(text_data, kmeans.labels_):
        alist.append([label, key])
    alist.sort()

    # выводим результат в таблице
    return render_template('table.html', data=alist)


@app.route('/increase_data_form')
def increase_data_form():
    return render_template('increase_data_form.html')


@app.route('/increase_data_table', methods=['POST'])
def increase_data_table():
    query, mark = request.form['query'], request.form['mark']
    # вытаскиваем данные
    f = open('db.txt', 'r', encoding='utf-8')
    data = f.read().split('\n')[:-1]
    print('data:',data)
    text_data = data.copy()
    data.append(query)
    print('data:', data)

    # разделяем на кластеры
    tf = TfidfVectorizer(min_df=1) # Объект с помощью которого мы проведём векторизацию
    
    data = tf.fit_transform(data)
    kmeans = KMeans(n_clusters=2, n_init=10, max_iter=300).fit(data)
    query_claster = kmeans.labels_[-1]

    alist = []

    for key, label in zip(text_data, kmeans.labels_):
        alist.append([label, key])

    for item in alist:
        if item[0] == query_claster:
            item.append(mark)
            print('we are here1')
        else:
            item.append('None mark')
            print('we are here 2')
    print(alist)
    return render_template('increase_data_table.html',data=alist, query=query, mark=mark)


'''<------handlers------>'''
@app.route('/handler1', methods=['POST'])
def handler1():
    f = open('db.txt', 'a', encoding='utf-8')
    f.write(str(request.form['search']) + '\n')
    f.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)