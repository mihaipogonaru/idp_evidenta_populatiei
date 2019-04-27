from flask import Blueprint, request, jsonify
from ..extensions import db

blueprint = Blueprint("user", __name__, url_prefix='/user')

@blueprint.route("/add/<string:email>", methods=['post'])
def add(email: str):
    req = request.get_json(silent=True)
    if not req:
        return jsonify({"error": "No JSON found in request"})

    if "password" not in req:
        return jsonify({"error": "Malformed JSON found in request"})

    try:
        db.insert_user(email, req["password"])
    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify({"msg": "User added successfully"})    


@blueprint.route("/view/<string:email>", methods=['get'])
def view(email: str):
    resp = {"error": "No error message"}

    try:
        resp = db.select_user(email)
    except Exception as e:
        resp = {"error": str(e)}

    if not resp:
        resp = {"error": "User not found"}

    return jsonify(resp) 


@blueprint.route("/viewall", methods=['get'])
def viewall():
    return jsonify(db.get_users())


@blueprint.route("/remove/<email:name>", methods=['post'])
def delete(email: str):
    resp = {"error": "No error message"}

    try:
        resp = db.delete_user(email)
    except Exception as e:
        resp = {"error": str(e)}

    if not resp:
        resp = {"error": "User not found"}

    return jsonify(resp) 
