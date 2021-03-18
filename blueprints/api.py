from flask import Flask, request, redirect, Blueprint
from april import material

api_blueprint = Blueprint("apibp", __name__) 

@api_blueprint.route("/apitest/", methods=["POST"])
def api():
    material.newMaterial(request.get_json()["name"], request.get_json()["title"], request.get_json()["content"])
    return "Sucess"

print("$ Api blueprint loaded!")