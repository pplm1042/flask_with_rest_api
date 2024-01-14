from flask import Flask, jsonify, render_template
import json

from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


# Get the environment variables
app.config['DEBUG'] = os.environ['FLASK_DEBUG']

@app.route('/')
def hello():

    data = {'code' : '40004', 'message' : '올바르지 않은 이메일', 'result' : {'is_sussess': False}}
    result = json.dumps(data, ensure_ascii=False)
    return result

if __name__ == '__main__':
    app.run()

