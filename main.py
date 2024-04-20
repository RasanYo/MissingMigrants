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




def run(article_title, article_content, start_date, end_date, max_results=5, number_of_queries_per_language=2, interested_languages=["english"]):
    open_ai_client = OpenAI()
    print("Generating queries...")
    query_gen = QueryGenerator(open_ai_client)
    queries = query_gen.generate_queries(article_title, interested_languages, number_of_queries_per_language)
    queries = json.loads(queries)
    similarity_checker = DocumentSimilarity(open_ai_client)
    data = process_data(queries, available_languages, article_title, max_results, start_date, end_date,similarity_checker, article_content)
    
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
            


def process_data(data, available_languages, initial_prompt,max_results=1, start_date=(2022, 5, 1), end_date=(2022, 5, 20), similarity_checker=None, article_content=None):
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
    article_content = """On Monday, Tunisia's coastguard retrieved the bodies of five migrants, raising the week's death toll to 11. They also rescued a total of 663 migrants, reflecting a surge in crossings from North Africa to Italy due to improved weather.

The coastguard reported on Monday that five bodies were recovered near the coastal city of Sfax. In the past four days, a total of 11 migrants have been found dead in the area.

Tunisian security forces have also prevented 3,058 migrants from crossing to Europe by boat since Friday. The majority of them are said to have come from sub-Sahara Africa.

On Monday alone, 633 people were stopped from setting off by boat from Tunisia towards Europe following a rescue mission. Security forces also reportedly arrested 120 smugglers.

Additionally, a shipwreck off the Italian coast over the weekend likely resulted in the death of a 15-month-old girl.

Also read: 17 Tunisian migrants missing at sea as reported deaths reach record high

Oil tanker rescues refugees
In the early hours of Monday, an oil tanker in the Mediterranean Sea picked up 139 people from an unseaworthy vessel on their way to Europe from Libya, Italian authorities reported.

During the rescue operation, three migrants fell into the water and remain missing at sea. The initial search for them was unsuccessful, according to reports.

The rest of the rescued migrants were taken by the Italian coastguard to the Italian Mediterranean island of Lampedusa. The migrants were said to have originated from various African countries, as well as from Syria, Pakistan, and Bangladesh.

Lampedusa, situated between Sicily and Tunisia, has long been a focal point of the smuggling trade. Reports indicate that passengers paid between $3,000 and $7,000 for the dangerous journey on the 12-meter boat.

Also read: EU-Tunisia migration deal: Encouraging the people smugglers?

New agreements on migration and labor
Under a recent agreement signed between the Italian and Albanian governments, rescued migrants from the Mediterranean could soon increasingly be taken to Albania for processing -- instead of remaining at a reception center in Lampedusa before being transferred to the Italian mainland. Two reception centers and a repatriation center are scheduled to open in Albania in May to facilitate this process.

This comes after the EU reached a controversial agreement with Tunisia late last year: in exchange for millions of euros in financial aid, the North African country is expected to take stronger action against traffickers and illegal crossings. However, there have been doubts about the sustainability of this agreement.

Earlier this year, Italy and Tunisia also signed a deal to bring 12,000 Tunisian workers to Italy over the next three years. Under the deal, Italian and Tunisian labor organizations, Sviluppo Lavoro Italia and Aneti, will collaborate to identify the workforce requirements of the Italian market and the Tunisian workers who could meet those demands.

Also read: EU criticized over migration deal with Egypt

Fewer crossings compared to last year
According to the Tunisian Forum for Economic and Social Rights (FTDES), over 1,300 migrants attempting to cross to Europe from the coast of Tunisia were killed in 2023.

Compared to last year, the number of migrants arriving in Italy via the central Mediterranean route, mostly from Tunisia and Libya, has meanwhile decreased.

The Italian Interior Ministry counted nearly 9500 people reaching Italy by sea so far this year, compared to over 20,000 in the same period last year."""
    max_results = 5
    number_of_queries_per_language = 2
    interested_languages = ["english", "spanish", "french", "arabic", "italian", "greek"]
    start_date = (2024, 3, 23)
    end_date = (2024, 3, 28)
    run(
        article_title=article_title,
        article_content=article_content,
        start_date=start_date,
        end_date=end_date,
        max_results=max_results,
        number_of_queries_per_language=number_of_queries_per_language,
        interested_languages=interested_languages
    )