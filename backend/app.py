from flask import Flask, jsonify, request
import json
import os
app = Flask(__name__)



def transform_json(original_json):
    items = []
    
    # Loop through each category in the original JSON
    for language in original_json.values():
        print(language)
        for category, articles in language.items():
            # Process each article
            for article in articles:
                # Extract necessary details
                item = {
                    "title": article.get("title"),
                    "description": article.get("article", {}).get("text"),
                    "url": article.get("url")
                }
                # Add the item to the list
                items.append(item)



    
@app.route("/")
def home():
    return "Hello, World!"

@app.route("/api/search", methods=["POST"])
def search():
    data = request.json  # This will contain the data sent from the frontend
    search_keywords = data.get('keywords')  # Assuming 'keywords' is what you're sending
    # Here, you can add logic to process these keywords
    modified_keywords = search_keywords + "  language:" + data.get('language') + "  start date:" + data.get('startDate')+ "  end date:" + data.get('endDate')

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


@app.route("/api/healthchecker", methods=["GET"])
def healthchecker():

    return {"status": "success", "message": "Integrate Flask Framework with Next.js"}

 
if __name__ == "__main__":
    app.run(debug=False)
 