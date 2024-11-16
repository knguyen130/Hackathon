from flask import Flask
from flask import render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def page1():
    return send_from_directory('static', "index.html")


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25565)
