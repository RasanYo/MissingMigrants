import json
from datetime import datetime, timedelta
from collections import defaultdict

def categorize_entries(data, date_range_days):
    categories = defaultdict(list)
    for lang, item in data.items():
        for i in item['data']:
            new_key = (i['published date'], i['vector']['Country of Incident'])
            i["language"] = lang
            i["query"] = item['query']
            
            found = False

            # Iterate over existing keys to see if this should be grouped with them
            for existing_key in list(categories.keys()):
                existing_date, existing_country = existing_key
                # Check if the country matches and the date is within the specified range
                if existing_country == new_key[1] and date_in_range(existing_date, new_key[0], date_range_days):
                    categories[existing_key].append(i)
                    found = True
                    break

            # If no suitable existing category is found, create a new category
            if not found:
                categories[new_key].append(i)
    
    # Debugging output to check the categorization
    for key, items in categories.items():
        print(f"Key: {key}, Entries: {len(items)}")

    
    new_data = {}
    for (date, country), items in categories.items():
        new_data[f"({date}, {country})"] = items
        # for item in items:
        #     item['language'] = ""  # assuming the language needs to be filled or modified
        #     new_data['category']['data'].append(item)
    
    return new_data

def date_in_range(original_date, new_date, num_days):
    """
    Check if the 'new_date' is within 'num_days' of 'original_date'
    - original_date: 'DD/MM/YYYY'
    - new_date: 'DD/MM/YYYY'
    - num_days: int 
    
    return: bool
    """
    # Format for parsing the dates
    date_format = "%d/%m/%Y"

    try:
        # Convert the string dates to datetime objects
        original_datetime = datetime.strptime(original_date, date_format)
        new_datetime = datetime.strptime(new_date, date_format)
    except ValueError:
        # This exception handles cases where the date format is incorrect
        raise ValueError("Incorrect date format, should be DD/MM/YYYY")

    # Calculate the difference in days between the two dates
    date_difference = abs((new_datetime - original_datetime).days)

    # Check if the difference is within the allowed number of days
    return date_difference <= num_days

# Example usage:
# Assuming `input_json` is your JSON string read from a file or other source
if __name__ == "__main__":
    with open('../data/Five migrants found dead off the coast of Tunisia_all_languages.json') as f:
        input_json = json.load(f)

    # print(input_json)
    transformed_json = categorize_entries(input_json)
    with open('./transformed.json', 'w') as f:
        json.dump(transformed_json, f, indent=4)
