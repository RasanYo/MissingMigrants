import json

def group_by_criteria(queries):
    # Dictionary to hold the categories based on 'published date' and 'Country of Incident'
    categories = {}

    # Iterate through each key in the dictionary of queries
    for language, data in queries.items():
        print(type(data))
        for article in data:
            print(article)
            # Extract the key criteria
            published_date = article['published date']
            country_of_incident = article['vector']['Country of Incident']

            # Create a unique key for each category
            category_key = (published_date, country_of_incident)
            
            if category_key not in categories:
                categories[category_key] = {
                    'query': []
                }
            
            # Modify entry to include the language key
            data_with_language = article
            data_with_language['language'] = language
            
            # Append the item to the correct category
            categories[category_key]['query'].append(data_with_language)

    # Create the final structured output
    output = {
        'category': {}
    }
    
    # Assign each category to output with a key or to unknown/mixed
    unknown_mixed = {'query': []}
    for key, value in categories.items():
        if key[0] and key[1]:  # Both published date and country of incident are present
            output['category'][f'{key[0]}_{key[1]}'] = value
        else:
            unknown_mixed['query'].extend(value['query'])
    
    # Include unknown/mixed category if there are any such items
    if unknown_mixed['query']:
        output['category']['unknown/mixed'] = unknown_mixed
    
    return output



# Example usage:
# Assuming `input_json` is your JSON string read from a file or other source
if __name__ == "__main__":
    with open('../data/Five migrants found dead off the coast of Tunisia_all_languages.json') as f:
        input_json = json.load(f)

    # print(input_json)
    transformed_json = group_by_criteria(input_json)
    print(transformed_json)
