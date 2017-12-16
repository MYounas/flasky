
from flask import Flask,make_response

app=Flask(__name__)


@app.route('/')
def index():
    # return '<h1>Hello world!</h1>'
    response=make_response('<h1>Hello world!</h1>')
    response.set_cookie('a','3')

    return response

@app.route('/user/<name>')
def user(name):
    return '<h1>hello {0}'.format(name)


if __name__=='__main__':
    app.run(debug=True)