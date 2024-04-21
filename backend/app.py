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

    print(start_date)
    
    language= data.get('language')
    print(language)
    #start_date = datetime.strptime(data.get('startDate'), date_format)
    #end_date = datetime.strptime(data.get('endDate'), date_format)
    #languages = [data.get('language')]

    # Simulating a delay of 2 seconds

    # Here, you can add logic to process these keywords
    #modified_keywords = search_keywords + "  language:" + data.get('language') + "  start date:" + data.get(
      #  'startDate') + "  end date:" + data.get('endDate')

    #return jsonify({"status": "success", "original": search_keywords, "modified": modified_keywords})
    json_path = "../data/DEMO2_transformed.json"

    try:
        with open(json_path, 'r') as file:
            migrants_data = json.load(file)
    except Exception as e:
        # Log the exception message
        print(f"Error loading JSON data: {str(e)}")
        return jsonify({"status": "error", "message": f"Error loading data: {str(e)}"}), 500
    # print(transform_json(migrants_data))
    # Return the loaded JSON data

    # migrants_data= run(query, start_date,end_date,max_results=5, number_of_queries_per_language=2,
    #     interested_languages=language)
    return migrants_data



@app.route("/api/healthchecker", methods=["GET"])
def healthchecker():
    return {"status": "success", "message": "Integrate Flask Framework with Next.js"}


if __name__ == "__main__":
    app.run(debug=False)
