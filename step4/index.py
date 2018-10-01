from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template

from DataStore.MySQL import MySQL

app = Flask(__name__)

@app.route('/')
def main():
    props = {'title': 'Step-by-Step Flask - index', 'msg': 'Welcom to Index Page.'}
    html = render_template('index.html', props=props)
    return html

@app.route('/hello')
def hello():
    props = {'title': 'Step-by-Step Flask - hello', 'msg': 'Hello World.'}
    html = render_template('hello.html', props=props)
    return html

@app.route('/users')
def users():
    props = {'title': 'Users List', 'msg': 'Users List'}
    dns = {
        'user': 'mysql',
        'host': 'localhost',
        'database': 'kaggle'
    }
    db = MySQL()
    db.open(**dns)
    sql = 'SELECT * FROM users'
    users = db.query(sql)
    db.close()
    html = render_template('users.html', props=props,users=users)
    return html

@app.route('/users/<id>')
def user(id):
    props = {'title': 'User Infomation', 'msg': 'User Infomation'}
    dns = {
        'user': 'mysql',
        'host': 'localhost',
        'database': 'kaggle'
    }
    db = MySQL()
    db.open(**dns)
    sql = 'SELECT * FROM users WHERE id = ?'
    data = db.query(sql, id, prepared=True)
    user = [bary.decode('utf-8') if isinstance(bary, bytearray) else bary for bary in data[0]]
    db.close()
    html = render_template('user.html', props=props,user=user)
    return html

@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)
