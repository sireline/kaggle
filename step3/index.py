from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template

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

@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)
