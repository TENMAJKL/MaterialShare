from flask import Flask, Blueprint, redirect
from april import materials
search = Blueprint("searchbp", __name__) 

@search.route('/search/<term>')
def searchPage(term):
  searched = materials.getBySearch(term.replace("+", " "))
  print(searched)
  if len(searched) == 0:
    searched = "toto jsem nenasel je mi to lito"
  else:
    searched = str(searched)
  
  return searched

@search.route("/search/")
def searchReturn():
  return redirect("/")