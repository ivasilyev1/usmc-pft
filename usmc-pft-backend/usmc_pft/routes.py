from flask import jsonify, request
from flask_cors import cross_origin
from usmc_pft import app
from usmc_pft.data_access.pft_data_access import get_pft_score
from usmc_pft.data_access.cft_data_access import get_cft_score

# Email address is added by frontend to create a "mailto:" <a> tag.
error_message = {"error": "Unable to process your score data. Please verify your inputs and try again."}

@app.route("/api/pft", methods=['POST'])
@cross_origin(origins="http://localhost:*")
def usmc_pft():
    request_body = request.get_json()
    score = None
    try:
        app.logger.info(f'Request PFT score for event info: {request_body}')
        score = get_pft_score(request_body)
    except Exception as e:
        app.logger.exception(f'Encountered an error while processing PFT scores')
        return jsonify({"score": error_message}), 500

    app.logger.info(f'Calculated scores: {score}')

    return jsonify({"score" : score}), 200

@app.route("/api/cft", methods=['POST'])
@cross_origin(origins="http://localhost:*")
def usmc_cft():
    request_body = request.get_json()
    score = None
    try:
        app.logger.info(f'Request CFT score for event info: {request_body}')
        score = get_cft_score(request_body)
    except:
        app.logger.exception(f'Encountered an error while processing CFT scores')
        return jsonify({"score": error_message}), 500

    app.logger.info(f'Calculated scores: {score}')

    return jsonify({"score": score}), 200
