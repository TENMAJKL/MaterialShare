#Vitej v mainu, zde se budou registrovat blueprinty

print("Blueprints->\n")

from flask import Flask, request, render_template, session, redirect
from blueprints import index, search, register, login, profile, api
from april import notifications, user, dbuniversal, material
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os

print("<-\n")

load_dotenv() 

app = Flask(__name__) 

app.config["SECRET_KEY"] = os.getenv("SESSIONKEY")

csrf = CSRFProtect(app)

app.register_blueprint(index.index)
app.register_blueprint(search.search)
app.register_blueprint(register.register)
app.register_blueprint(login.login)
app.register_blueprint(profile.profile)
app.register_blueprint(api.api_blueprint)

csrf.exempt(api.api_blueprint)

@app.errorhandler(500)
def internal_error(e):
    notifications.errorHook(500, request.path)
    page = "https://materialshare.tenmajkl.repl.co" + str(request.path)
    return render_template("errors/500error.html", page = page)

@app.errorhandler(404)
def notfound(e):
  return render_template("errors/404error.html", page = request.path)

@app.errorhandler(405)
def methodnotallowed(e):
  notifications.errorHook(405, request.path)
  return render_template("errors/405error.html", page = request.path)

@app.route("/database", methods=["POST", "get"])
def test():
  if "name" in session:
    if user.getUser(session["name"]).getDbPerm(): 
      if request.method == "POST":
        if "drop" not in request.form.get("Command").lower():
            table = dbuniversal.loadCommand(request.form.get("Command"))
        else:
            table = [["vypada to ze toto tady nefunguje, zkusil bych pouzit pma..."]]
        return render_template("nwmSQL.html", table = table)
    else:
        return "za pokus to stalo"
    
    return render_template("nwmSQL.html")
  else:
      return redirect("/")


@app.route("/tutorial")
def tutorial():
  return render_template("tutorial.html")

@app.route("/500")
def e500():
  return render_template("errors/500error.html", page = request.path)

@app.route("/502")
def e502():
  return render_template("errors/502error.html", page = request.path)

@app.route("/405")
def e405():
  return render_template("errors/405error.html", page = request.path)

@app.route("/test")
def profile():
    text = "[ahoj]"
    return render_template("sandbox.html", text = text)

@app.route("/credits")
def credit():
    return render_template("credits.html")

@app.route("/art")
def art():
    return render_template("art.html")

@app.route("/upravit", methods=["POST", "GET"])
def upravit():
    return render_template("upravit-vlozit.html", action_name = 'Upravit', title="Lorem ipsum", content="Dolor sit amet ")

@app.route("/pridat", methods=["POST", "GET"])
def pridat():
    return render_template("upravit-vlozit.html", action_name = 'Přidat', title="", content="")


@app.route("/forgotten-password")
def forgottenpassword():
  return render_template("auth/forgotten-password.html")

@app.route("/profile")
def profile_view():
  return render_template("profile/profile.html", profilepicture=None)

#@app.route("/materials")
#def materials():
#  return render_template("searched_materials.html")

@app.route("/materials")
def materials():
  return render_template("materials/searched_materials.html", profilepicture=None)

@app.route("/game")
def game():
  if "name" in session:
    photo = user.getUser(session["name"]).getPhoto()
  else:
    photo = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fweneedfun.com%2Fwp-content%2Fuploads%2F2016%2F08%2FThe-Color-Black-9.jpg&f=1&nofb=1"
  return render_template("game.html", photo = photo)




app.run(host='0.0.0.0', port=5000) 

