from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from usmc_pft import app, db
from usmc_pft.data_access.pft_data_access import get_pft_score
from usmc_pft.data_access.cft_data_access import get_cft_score

error_message = {"error": "Unable to process your score data. Please verify your inputs and try again. If the error persists please contact "}

@app.route("/api/pft", methods=['POST'])
@cross_origin(origins="http://localhost:*")
def usmc_pft():
    request_body = request.get_json()
    score = None
    try:
        score = get_pft_score(request_body)
    except:
        return jsonify({"score": error_message}), 500
    return jsonify({"score" : score}), 200

@app.route("/api/cft", methods=['POST'])
@cross_origin(origins="http://localhost:*")
def usmc_cft():
    request_body = request.get_json()
    score = None
    try:
        score = get_cft_score(request_body)
    except:
        return jsonify({"score": error_message}), 500
    return jsonify({"score": score}), 200
