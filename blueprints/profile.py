from flask import Flask, request, render_template, session, Blueprint, redirect
from april import user
from hashlib import sha256

profile = Blueprint("profilebp", __name__) 

@profile.route("/profile/edit", methods=["GET", "POST"])
def profile_page():
  error = ""
  if "name" not in session:
    return redirect("/login/")
  else:
    user_session = session["name"]
    name = user_session
    user_db = user.getUser(user_session)
    email = user_db.getMail()
    description = user_db.getDescription()
    profilepicture = user_db.getPhoto()
    return render_template("profile/profile.html", name=name, email=email, description=description, profilepicture= profilepicture)
