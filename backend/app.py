from datetime import datetime
import time
from flask import Flask, jsonify, request
import json
from main import run

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/api/search", methods=["POST"])
def search():
    try:
        data = request.json
        query = data.get('keywords')
        date_format = "%Y-%m-%d"
        start_date = datetime.strptime(data.get('startDate'), date_format)
        end_date = datetime.strptime(data.get('endDate'), date_format)
        language = data.get('language')

        # Assume 'run' is a function that could potentially fail
        result = run(query, start_date, end_date, max_results=5, number_of_queries_per_language=2, interested_languages=language)
        return jsonify(result)
    except Exception as e:
        pass



@app.route("/api/healthchecker", methods=["GET"])
def healthchecker():
    return {"status": "success", "message": "Integrate Flask Framework with Next.js"}


if __name__ == "__main__":
    app.run(debug=False)
