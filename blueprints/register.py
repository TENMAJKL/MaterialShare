from flask import Flask, request, render_template, session, Blueprint, redirect
from april import user
from hashlib import sha256
import random

register = Blueprint("registerbp", __name__) 

salt_template = "1234567890qwertyuiopasdfghjklzxcvbnm"

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
          salt = "".join(random.sample(salt_template, 10))
          password = password + salt
          password = sha256(password.encode('utf-8')).hexdigest()
          user.register(name, password, salt, email)
          session["name"] = name
          return("dobra prace")
      else:
        error = "Hesla se neshodují, nebo je jméno stejné jako heslo"
        


  return render_template("auth/register.html", error = error)

print("$ Register blueprint loaded!")