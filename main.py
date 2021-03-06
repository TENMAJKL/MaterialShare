#Vitej v mainu, zde se budou registrovat blueprinty

from flask import Flask, render_template, request
from april import user, notifications
import time
app = Flask(__name__) 

@app.route('/') 
def main(): 
  return render_template("index.html")


@app.errorhandler(500)
def internal_error(e):
    notifications.errorHook(500, request.path)
    return "error 500 o chybe vim jak neovim"

@app.errorhandler(502)
def gateway(e):
    notifications.errorHook(502, request.path)
    return "502 vim jak neovim o tom uy dik fik"


app.run(host='0.0.0.0', port=5000) 

