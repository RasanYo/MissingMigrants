import json
from collections import defaultdict

def categorize_entries(data):
    # Creating a dictionary to hold categories based on date and country of incident
    categories = defaultdict(list)
    # Iterating through each item in the provided data list
    for item in data:
        # Creating a unique key for each category based on published date and country of incident
        key = (item['published date'], item['vector']['Country of Incident'])
        
        # Appending the item to the correct category list in the dictionary
        categories[key].append(item)
    # Initializing a new structure to hold the formatted data
    new_data = {
        'category': {
            'query': "",
            "data": []
        }
    }
    # Processing categorized items to format according to the new required JSON structure
    for (date, country), items in categories.items():
        # Each category becomes an entry in the 'data' list
        for item in items:
            # Modifying the item to include 'language' and adjusting 'vector' if necessary
            item['language'] = ""  # assuming the language needs to be filled or modified
            new_data['category']['data'].append(item)
    # Handling any uncategorized or 'unknown/mixed' categories if needed
    # Assuming all entries are properly categorized by the previous logic
    # If necessary, add logic here to handle uncategorized items
    return new_data

def main():
    # Example usage
    # Assuming 'input_data' is your JSON object read from a file or elsewhere
    input_json = """
    {
        "language": {
            "query": "query 1",
            "data": [
                {
                    "title": "Example Title",
                    "description": "Example Description",
                    "published date": "2024-04-20",
                    "url": "http://example.com",
                    "publisher": {
                        "href": "http://publisher.com",
                        "title": "Example Publisher"
                    },
                    "article": {
                        "title": "Article Title",
                        "text": "Example text of the article."
                    },
                    "vector": {
                        "Region of Incident": "Example Region",
                        "Incident Date": "2024-04-19",
                        "Number of Dead": 10,
                        "Minimum Estimated Number of Missing": 5,
                        "Total Number of Dead and Missing": 15,
                        "Number of Survivors": 3,
                        "Number of Females": 2,
                        "Number of Males": 8,
                        "Number of Children": 4,
                        "Country of Origin (of the people)": "Exampleland",
                        "Region of Origin (of the people)": "Example Region",
                        "Cause of Death": "Example Cause",
                        "Country of Incident": "Country X",
                        "Migration Route": "Example Route",
                        "Location of Incident": "Example Location"
                    }
                }
            ]
        }
    }
    """

    # Convert the JSON string into a Python dictionary
    input_data = json.loads(input_json)

    # Get the 'data' list from the original JSON structure
    original_data = input_data['language']['data']

    # Process the data to categorize and reformat
    new_data = categorize_entries(original_data)

    # Convert the new data dictionary back to JSON
    output_json = json.dumps(new_data, indent=4)
    print(output_json)

if __name__ == "__main__":
    main()
