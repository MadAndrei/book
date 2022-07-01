import sqlite3
from flask import Flask, g

DATABASE = 'wikibooks.db'
app = Flask(__name__)


@app.route('/')
def hello_world():
    cur = get_db().cursor()
    titles = {}
    for i, row in enumerate(cur.execute('SELECT title FROM en LIMIT 4')):
        titles['title' + str(i)] = row
    return titles


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    """Закрывает соединение с с БД"""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)

