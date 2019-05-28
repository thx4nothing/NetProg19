#!.env/bin/python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "Hallo Welt!"

@app.route('/add/<one>/<two>')
def add(one, two):
    # show the user profile for that user
    erg = int(one) + int(two)
    return '= %d' % erg

@app.route('/sub/<one>/<two>')
def sub(one, two):
    # show the user profile for that user
    erg = int(one) - int(two)
    return '= %d' % erg

@app.route('/div/<one>/<two>')
def div(one, two):
    # show the user profile for that user
    erg = int(one) / int(two)
    return '= %d' % erg

@app.route('/mul/<one>/<two>')
def mul(one, two):
    # show the user profile for that user
    erg = int(one) * int(two)
    return '= %d' % erg

