
#Vitej v mainu, zde se budou registrovat blueprinty

from flask import Flask, request, render_template, session
from blueprints import index, search, register, login, profile
from april import notifications
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__) 

app.config["SECRET_KEY"] = "78as465das7d86as4as65as4d5asd4as56as87das4ads56asd4as56dasd56asd5as4d56"

csrf = CSRFProtect(app)

app.register_blueprint(index.index)
app.register_blueprint(search.search)
app.register_blueprint(register.register)
app.register_blueprint(login.login)
app.register_blueprint(profile.profile)


@app.errorhandler(500)
def internal_error(e):
    notifications.errorHook(500, request.path)
    page = "https://materialshare.tenmajkl.repl.co" + str(request.path)
    return render_template("500error.html", page = page)

@app.errorhandler(404)
def notfound(e):
  return render_template("404error.html", page = request.path)

@app.errorhandler(405)
def methodnotallowed(e):
  notifications.errorHook(405, request.path)
  return render_template("405error.html", page = request.path)

@app.route("/test")
def test():
  text = "while True: \n  print(Majkl ja kkt xdddddddd)"
  return render_template("sandbox.html", text = text)

@app.route("/tutorial")
def tutorial():
  return render_template("tutorial.html")



@app.route("/profile")
def profile():
  return render_template("profile.html")

@app.route("/forgotten-password")
def forgottenpassword():
  return render_template("forgotten-password.html")

@app.route("/materials")
def materials():
  return render_template("materials.html")

@app.route("/game")
def game():
  return render_template("game.html")

app.run(host='0.0.0.0', port=5000) 

