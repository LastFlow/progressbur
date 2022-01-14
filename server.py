from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    print("kjoasdjasdjasl") 
    app.run(host='127.0.0.1', port='48150', debug=True)