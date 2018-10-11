from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request

from DataStore.MySQL import MySQL

dns = {
    'user': 'mysql',
    'host': 'localhost',
    'password': 'NewPassword',
    'database': 'kaggle'
}
db = MySQL(**dns)
app = Flask(__name__)

@app.route('/')
def main():
    props = {
        'title': 'Step-by-Step Flask - index',
        'breadcrumb': [
            {'href': '/', 'caption': 'Home'}
        ],
        'msg': 'Welcom to Index Page.',
        'table_contents': [
            {'href': '/users', 'caption': 'Users List'},
            {'href': '/hello', 'caption': 'About me'}
        ]
    }
    html = render_template('index.html', props=props)
    return html

@app.route('/hello')
def hello():
    props = {
        'title': 'Step-by-Step Flask - hello',
        'breadcrumb': [
            {'href': '/', 'caption': 'Home'},
            {'href': '/hello', 'caption': 'About me'}
        ],
        'msg': 'Hello World.'
    }
    html = render_template('hello.html', props=props)
    return html

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        user_data = []
        user_data.append(request.form['last_name'] + " " + request.form['first_name'])
        user_data.append(request.form['age'])
        user_data.append(request.form['gender'])
        stmt = 'INSERT INTO users (name, age, gender) VALUES (?, ? ,?)'
        result = db.insert(stmt, *tuple(user_data), prepared=True)
    stmt = 'SELECT * FROM users'
    users = db.select(stmt)

    def _page_range():
        p = round(len(users)/10)
        if p <= 1:
            return (1,)
        elif p <= 10:
            return range(1, p+1)
        else:
            return range(1, 11)

    props = {
        'title': 'Users List',
        'breadcrumb': [
            {'href': '/', 'caption': 'Home'},
            {'href': '/users', 'caption': 'Users List'}
        ],
        'pages': {
            'page_range': _page_range(),
            'page_size': 10,
            'prev': 'disabled',
            'next': 'disabled',
            'view_rows': [10, 25, 50]
        },
        'msg': 'Users List'
    }
    html = render_template('users.html', props=props, users=users)
    return html

@app.route('/users/<int:id>', methods=['GET','PUT','DELETE'])
def user(id):
    props = {
        'title': 'User Information',
        'breadcrumb': [
            {'href': '/', 'caption': 'Home'},
            {'href': '/users', 'caption': 'Users List'},
            {'href': '/users/'+str(id), 'caption': 'User Information'}
        ],
        'msg': 'User Information'
    }
    if request.method == 'DELETE':
        stmt = 'DELETE FROM users WHERE id = ?'
        result = db.delete(stmt, id, prepared=True)
        redirect(url_for('users'))
    elif request.method == 'PUT':
        user_data = []
        user_data.append('id')
        user_data.append(request.form['last_name'] + " " + request.form['first_name'])
        user_data.append(request.form['age'])
        user_data.append(request.form['gender'])
        stmt = 'UPDATE users SET name=?, age=?, gender=? WHERE id = ?'
        result = db.update(stmt, *user_data, prepared=True)
    stmt = 'SELECT * FROM users WHERE id = ?'
    user = db.select(stmt, id, prepared=True)
    html = render_template('user.html', props=props,user=user[0])
    return html

@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)
