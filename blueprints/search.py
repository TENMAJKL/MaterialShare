from flask import Flask, Blueprint, redirect, session, render_template
from april import materials, user
search = Blueprint("searchbp", __name__) 

@search.route('/search/<term>')
def searchPage(term):
  searched = materials.getBySearch(term.replace("+", " "))
  if len(searched) == 0:
    return "Bohuzel toto jsem nenasel"
  else:
    try:
      name = session["name"]
      profilepicture = user.getUser(name).getPhoto()
    except KeyError:
      name = ""
      profilepicture = ""
    return render_template("materials.html", name = name, profilepicture = profilepicture, searched_materials = searched, search = term)

@search.route("/search/")
def searchReturn():
  return redirect("/")


print("$ Search blueprint loaded!")