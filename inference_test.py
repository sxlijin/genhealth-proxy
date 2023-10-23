import unittest
import connexion
import json

class TestConnexionServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = connexion.FlaskApp(__name__, specification_dir='.', options={"swagger_ui": False})
        app.add_api('inference.yaml')  # Reference your OpenAPI specification
        cls.app = app.app.test_client()

    def test_good_request(self):
        good_request = {
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
        response = self.app.post('/predict', data=json.dumps(good_request), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_bad_request(self):
        good_request = {
            'history': [
                {
                    'system': 'age',
                    'display': '64',
                },
                {
                    'system': 'ICD10CM',
                    'display': 'Type 2 diabetes mellitus',
                },
                {
                    'system': 'ICD10CM',
                    'display': 'Type 2 diabetes mellitus with stable proliferative diabetic retinopathy, right eye',
                },
            ],
            'num_predictions': 1,
            'generation_length': 10,
            'inference_threshold': 0.95,
            'inference_temperature': 0.95,
        }
        response = self.app.post('/predict', data=json.dumps(good_request), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()['detail'], "'code' is a required property - 'history.0'")

if __name__ == '__main__':
    unittest.main()
