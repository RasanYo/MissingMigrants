from openai import OpenAI
from query_generation.query_generation import QueryGenerator
from news_scraping.src.scraper import Scraper
from summarizing_article.chatgpt.similarity import DocumentSimilarity
import json


import os
os.environ["OPENAI_API_KEY"] = "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"

available_languages = {'english': 'en', 'indonesian': 'id', 'czech': 'cs', 'german': 'de', 'spanish': 'es-419', 'french': 'fr',
    'italian': 'it', 'latvian': 'lv', 'lithuanian': 'lt', 'hungarian': 'hu', 'dutch': 'nl', 'norwegian': 'no',
    'polish': 'pl', 'portuguese brasil': 'pt-419', 'portuguese portugal': 'pt-150', 'romanian': 'ro', 'slovak': 'sk',
    'slovenian': 'sl', 'swedish': 'sv', 'vietnamese': 'vi', 'turkish': 'tr', 'greek': 'el', 'bulgarian': 'bg',
    'russian': 'ru', 'serbian': 'sr', 'ukrainian': 'uk', 'hebrew': 'he', 'arabic': 'ar', 'marathi': 'mr', 'hindi': 'hi',
    'bengali': 'bn', 'tamil': 'ta', 'telugu': 'te', 'malyalam': 'ml', 'thai': 'th', 'chinese simplified': 'zh-Hans',
    'chinese traditional': 'zh-Hant', 'japanese': 'ja', 'korean': 'ko'}




def run(article_title, start_date, end_date, max_results=5, number_of_queries_per_language=2, interested_languages=["english"]):
    open_ai_client = OpenAI()
    print("Generating queries...")
    query_gen = QueryGenerator(open_ai_client)
    queries = query_gen.generate_queries(article_title, interested_languages, number_of_queries_per_language)
    queries = json.loads(queries)
    similarity_checker = DocumentSimilarity(open_ai_client)
    data = process_data(queries, available_languages, article_title, max_results, start_date, end_date,similarity_checker)
    
def get_all_articles_text(data):
    texts = []
    titles = []
    for language in data:
        for query in data[language]:
            for article in data[language][query]:
                texts.append(article['article']['text'])
                titles.append(article['article']['title'])
    return texts, titles


def scrape_original_data(max_results=1, start_date=(2022, 5, 1), end_date=(2022, 5, 20), lang='en'):
    scraper = Scraper(max_results=1, start_date=start_date, end_date=end_date, language=lang)
    scraper.get_article_by_url("https://archive.fo/X6n4Z")
            


def process_data(data, available_languages, initial_prompt,max_results=1, start_date=(2022, 5, 1), end_date=(2022, 5, 20)):
    # Dictionary to hold all scraped results
    all_scraped_data = {}
    
    for lang, queries in data.items():
        # Dictionary to hold results for the current language
        lang_scraped_data = {}
        
        for key, query in queries.items():
            # Initialize the scraper for each query
            scraper = Scraper(max_results=max_results, start_date=start_date, end_date=end_date, language=available_languages[lang])
            print(f"Scraping for language: {lang}, query key: {key}, query: {query}")
            
            # Scrape the query and store the data
            scraped_data = scraper.scrape_for_query(query)
            # scraped_data["article"]["Relevant"] = similarity_checker.check_document_coherence(scraped_data["article"]["text"], article_content)
            lang_scraped_data[query] = scraped_data
        
        # Add the language-specific results to the main dictionary
        all_scraped_data[lang] = lang_scraped_data

    # Define the filename
    filename = f"./data/{initial_prompt}_all_languages.json"
    
    # Write the aggregated scraped data to file
    result = write_json_to_file(all_scraped_data, filename)

    
    # Print the result
    if result:
        print(f"Saved all query results in {filename}")
    else:
        print(f"Failed to save query results in {filename}")

    return all_scraped_data

# Note: Ensure that the Scraper class and write_json_to_file function are defined and implement the actual functionality.
 

def write_json_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except:
        return False

if __name__ == "__main__":
    article_title = "Five migrants found dead off the coast of Tunisia"
    max_results = 5
    number_of_queries_per_language = 2
    interested_languages = ["english", "spanish", "french", "arabic", "italian", "greek"]
    start_date = (2024, 3, 23)
    end_date = (2024, 3, 28)
    run(
        article_title=article_title,
        start_date=start_date,
        end_date=end_date,
        max_results=max_results,
        number_of_queries_per_language=number_of_queries_per_language,
        interested_languages=interested_languages
    )