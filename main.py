#Vitej v mainu, zde se budou registrovat blueprinty

from flask import Flask, render_template, request, redirect
from april import user, notifications, materials
import time
app = Flask(__name__) 

@app.route('/', methods=["POST", "GET"]) 
def main():
  if request.method == "POST":
    term = request.form.get("search-term")
    if len(term) > 3:
      return redirect("/search/"+term)

  return render_template("index.html")

@app.route('/search/<term>')
def search(term):
  searched = materials.getBySearch(term)
  print(searched)
  if len(searched) == 0:
    searched = "toto jsem nenasel je mi to lito"
  else:
    searched = str(searched)
  
  return searched

@app.route("/search/")
def searchRedirect():
  return redirect("/")

@app.errorhandler(500)
def internal_error(e):
    notifications.errorHook(500, request.path)
    return "error 500 o chybe vim jak neovim"

@app.errorhandler(502)
def gateway(e):
    notifications.errorHook(502, request.path)
    return "502 vim jak neovim o tom uy dik fik"


app.run(host='0.0.0.0', port=5000) 

