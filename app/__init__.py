from flask import Flask, render_template,redirect
from subprocess import call,Popen
from .utils import readconf,reset

app = Flask(__name__)

@app.route('/')
def indext():
    conf = readconf()
    password = conf['password']
    port = conf['port']
    host = {'ip':'ss.ibat.me',
            'password':password,
            'port':port}
    return render_template('index.html',host=host)

@app.route('/new/')
def refresh():
    reset()
    return redirect('/')
