from flask import Flask, request, render_template, session, Blueprint, redirect
from april import user
from hashlib import sha256

login = Blueprint("loginbp", __name__) 

@login.route("/login/", methods=["GET", "POST"])
def login_page():
  error = ""
  if "name" in session:
    return redirect("/profile/edit")
  else:
    if request.method == "POST":
      try:
        name = request.form.get("name")
        password = request.form.get("Password")
        
        password = password + user.getUser(name).getSalt() 

        password = sha256(password.encode('utf-8')).hexdigest()

        

        

        if password == user.getUser(name).getPassword():
          session["name"] = name
          return redirect("/profile")
        else:
          error = "Špatné jméno nebo heslo!"
      except:
        error = "Špatné jméno nebo heslo!"
  
        


  return render_template("auth/login.html", error = error)

print("$ Login blueprint loaded!\n")