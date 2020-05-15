from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from usmc_pft import app, db
from usmc_pft.data_access.pft_data_access import get_pft_score
from usmc_pft.data_access.cft_data_access import get_cft_score

@app.route("/api/pft", methods=['POST'])
@cross_origin(origin="localhost")
def usmc_pft():
    request_body = request.get_json()
    score = get_pft_score(request_body)
    return jsonify({"score" : score}), 200

@app.route("/api/cft", methods=['POST'])
@cross_origin(origin='localhost')
def usmc_cft():
    request_body = request.get_json()
    score = get_cft_score(request_body)
    return jsonify({"score": score}), 200
