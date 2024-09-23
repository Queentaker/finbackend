from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS
import logging
import pandas as pd
import numpy as np
from flask_compress import Compress

app = Flask(__name__)
CORS(app)
Compress(app)

logger = logging.getLogger("Finan")
logger.setLevel(logging.DEBUG)

@app.route("/")
def index():
    return {"message": "Hello World!"}

data = pd.DataFrame({
    'x': [1, 2, 3],
    'y': [4, 9, 6]
})

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "up"}), 200

# New API route for retrieving the stored x and y values
@app.route("/data", methods=["GET"])
def get_data():
    # Convert the Pandas DataFrame to a dictionary for JSON serialization
    data_dict = data.to_dict(orient="records")
    return jsonify(data_dict), 200