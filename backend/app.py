from flask import Flask, jsonify, request
import json
import os
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"

@app.route("/api/search", methods=["POST"])
def search():
    data = request.json  # This will contain the data sent from the frontend
    search_keywords = data.get('keywords')  # Assuming 'keywords' is what you're sending
    # Here, you can add logic to process these keywords
    modified_keywords = search_keywords + "  language:" + data.get('language') + "  start date:" + data.get('startDate')+ "  end date:" + data.get('endDate')
    print(345)

    return jsonify({"status": "success", "original": search_keywords, "modified": modified_keywords})

@app.route("/api/healthchecker", methods=["GET"])
def healthchecker():
    return {"status": "success", "message": "Integrate Flask Framework with Next.js"}

 
if __name__ == "__main__":
    app.run(debug=False)
 