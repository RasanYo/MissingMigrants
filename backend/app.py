from datetime import datetime
from flask import Flask, jsonify, request
import json
from main import run

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/api/search", methods=["POST"])
def search():
    data = request.json  # This will contain the data sent from the frontend
    search_keywords = data.get('keywords')  # Assuming 'keywords' is what you're sending
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(data.get('startDate'), date_format)
    end_date = datetime.strptime(data.get('endDate'), date_format)
    languages = data.get('language')

    # Specify the path to your JSON file
    json_file_path = "./../data/message.json"

    # Open the JSON file and load its contents
    with open(json_file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    output = data
    # output = run(search_keywords, start_date, end_date, interested_languages=languages)

    return output


@app.route("/api/healthchecker", methods=["GET"])
def healthchecker():
    return {"status": "success", "message": "Integrate Flask Framework with Next.js"}


if __name__ == "__main__":
    app.run(debug=False)
