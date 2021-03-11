from flask import Flask, request, render_template, session, Blueprint, redirect
from april import user
from hashlib import sha256

register = Blueprint("registerbp", __name__) 

@register.route("/register/", methods=["GET", "POST"])
def register_page():
  if "name" in session:
    return redirect("/profile/edit")
  else:
    error = ""
    if request.method == "POST":
      name = request.form.get("name")
      password = request.form.get("Password")
      password2 = request.form.get("Password2")
      email = request.form.get("mail")
      
      if password == password2 and password != name:
        exist = user.nameInDb(name)
        mailexist = user.mailInDb(email)
        if exist and mailexist:
          error = "Bohužel, toto jméno už je zabrané."
        else:
          password = sha256(password.encode('utf-8')).hexdigest()
          user.register(name, password, email)
          session["name"] = name
          return("dobra prace")
      elif "@" not in email:
        error = "Neplatná  adresa!"
      else:
        error = "Hesla se neshodují, nebo je jméno stejné jako heslo"
        


  return render_template("registre.html", error = error)

print("$ Register blueprint loaded!")