import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False, methods=['GET'])
def get_version():
    return "{ \"api\": \"cool-api\", \"alive\": \"YES!!!\" }"

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=5050)
