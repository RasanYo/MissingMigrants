import json
from collections import defaultdict

def categorize_entries(data):
    categories = defaultdict(list)
    for lang, item in data.items():
        for i in item['data']:
            key = (i['published date'], i['vector']['Country of Incident'])
            i["language"] = lang
            i["query"] = item['query']
            categories[key].append(i)

    for (date, country), items in categories.items():
        print(len(items))
        # print(categories[(date, country)])
    # print(categories)
    
    new_data = {}
    for (date, country), items in categories.items():
        new_data[f"({date}, {country})"] = items
        # for item in items:
        #     item['language'] = ""  # assuming the language needs to be filled or modified
        #     new_data['category']['data'].append(item)
    
    return new_data

# Example usage:
# Assuming `input_json` is your JSON string read from a file or other source
if __name__ == "__main__":
    with open('../data/Five migrants found dead off the coast of Tunisia_all_languages.json') as f:
        input_json = json.load(f)

    # print(input_json)
    transformed_json = categorize_entries(input_json)
    with open('./transformed.json', 'w') as f:
        json.dump(transformed_json, f, indent=4)
