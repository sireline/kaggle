from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    props = {'title': 'Step-by-Step Flask', 'msg': 'Hello World.'}
    html = render_template('hello.html', props=props)
    return html

if __name__ == '__main__':
    app.run(debug=True)
