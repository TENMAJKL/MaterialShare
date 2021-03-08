from flask import Flask, render_template, request, redirect, Blueprint
index = Blueprint("indexbp", __name__) 

@index.route('/', methods=["POST", "GET"]) 
def main():
  if request.method == "POST":
    term = request.form.get("search-term")
    if len(term) > 3:
      return redirect("/search/"+term.replace(" ", "+"))

  return render_template("index.html")
