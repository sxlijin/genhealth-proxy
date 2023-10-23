import requests
from pprint import pprint

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token gh_s_k-YTA1NmU1NDYtMjExMi00YjljLTg0NmYtZDU2NTczMWUxYThk',
}

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

response = requests.post('https://api.genhealth.ai/predict', headers=headers, json=json_data)

pprint(response.json(), None, 2) 

fake_response = { 'history': [ {'code': '64', 'display': '64', 'system': 'age'},
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

response = requests.post('https://api.genhealth.ai/predict', headers=headers, json=json_data)

