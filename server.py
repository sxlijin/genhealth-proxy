from flask import Flask, request, jsonify
from connexion import FlaskApp
import json

app = FlaskApp(__name__, specification_dir='.', options={"swagger_ui": False})
app.add_api("/home/sxlijin/genhealth-proxy/inference.yaml")

# Sample data (in-memory data store)
items = []

json_data = {
    'history': [
        {
            'code': '64',
            'system': 'age',
            'display': '64',
        },
        {
            'code': 'E11',
            'system': 'ICD10CM',
            'display': 'Type 2 diabetes mellitus',
        },
        {
            'code': 'E11.3551',
            'system': 'ICD10CM',
            'display': 'Type 2 diabetes mellitus with stable proliferative diabetic retinopathy, right eye',
        },
    ],
    'num_predictions': 1,
    'generation_length': 10,
    'inference_threshold': 0.95,
    'inference_temperature': 0.95,
}

fake_inference_response = {
  'history': [ {'code': '64', 'display': '64', 'system': 'age'},
               { 'code': 'E11',
                 'display': 'Type 2 diabetes mellitus',
                 'system': 'ICD10CM'},
               { 'code': 'E11.3551',
                 'display': 'Type 2 diabetes mellitus with stable '
                            'proliferative diabetic retinopathy, right eye',
                 'system': 'ICD10CM'}],
  'predictions': [ [ { 'code': '00-01-month',
                       'display': '00-01-month',
                       'system': 'timegap'},
                     { 'code': 'E11',
                       'display': 'Type 2 diabetes mellitus',
                       'system': 'ICD10CM'},
                     { 'code': 'E11',
                       'display': 'Type 2 diabetes mellitus',
                       'system': 'ICD10CM'},
                     { 'code': 'isopropyl',
                       'display': 'isopropyl',
                       'system': 'RXNORM-FREETEXT'},
                     { 'code': 'A4452',
                       'display': 'Tape, waterproof, per 18 square inches',
                       'system': 'HCPCS'},
                     { 'code': 'E11',
                       'display': 'Type 2 diabetes mellitus',
                       'system': 'ICD10CM'}]]}

# Endpoint to get a list of items
#@app.route('/inference', methods=['POST'])
def inference():
    return jsonify(fake_inference_response)

if __name__ == '__main__':
    app.run(debug=True)
