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
    languages = [data.get('language')]

    # Simulating a delay of 2 seconds
    time.sleep(2)

    # Here, you can add logic to process these keywords
    modified_keywords = search_keywords + "  language:" + data.get('language') + "  start date:" + data.get(
        'startDate') + "  end date:" + data.get('endDate')

    #return jsonify({"status": "success", "original": search_keywords, "modified": modified_keywords})
    json_path = "/Users/eliotullmo/Documents/ETHZ/datathon/MissingMigrants/backend/data/Migrants dead trying to cross the Mediterranean Sea in Italy_all_languages.json"

    try:
        with open(json_path, 'r') as file:
            migrants_data = json.load(file)
    except Exception as e:
        # Log the exception message
        print(f"Error loading JSON data: {str(e)}")
        return jsonify({"status": "error", "message": f"Error loading data: {str(e)}"}), 500
    #print(transform_json(migrants_data))
    # Return the loaded JSON data
    return migrants_data

    return output


@app.route("/api/healthchecker", methods=["GET"])
def healthchecker():
    return {"status": "success", "message": "Integrate Flask Framework with Next.js"}


if __name__ == "__main__":
    app.run(debug=False)
