from flask import Flask, render_template,redirect, request, abort, send_from_directory, send_file
from subprocess import call,Popen
from .utils import readconf,reset

app = Flask(__name__)

app.config['DOWNLOAD_FOLDER'] = '/root/ssserver/files/'

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
