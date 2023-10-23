from flask import Flask, request, jsonify
from connexion import FlaskApp
import json

app = FlaskApp(__name__, specification_dir='.', options={"swagger_ui": False})
app.add_api("inference.yaml")

if __name__ == '__main__':
    app.run(debug=True)
