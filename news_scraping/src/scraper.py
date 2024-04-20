from gnews import GNews
import json
from datetime import datetime
from info_extractor.src.info_extracter import OpenAIInfoExtractor
import time

TIMEOUT = 10
class Scraper:
    
    def __init__(self, **kargs):
        self.google_news = GNews(**kargs)
        self.extractor = OpenAIInfoExtractor()

    def set_gnews(self, gnews):
        self.google_news = gnews

    def get_query_response(self, query):
        return self.google_news.get_news(query) 

    def get_article(self, resp):
        try:
            article = self.google_news.get_full_article(resp['url']) 
            start_time = time.time()
            while (article is None):
                if time.time() - start_time > TIMEOUT:
                    print(f"[TIMEOUT] Aborting scrape for {resp['title']}")
                    break  # Exit the loop if more than 5 seconds have passed
                else: pass
            vector = self.extractor.run(f"{article.title}\n{article.text}")
            print(f"\n[ARTICLE] {article.title}")
            resp["published date"] = self._convert_date_format(resp["published date"])
            resp["article"] = {
                'title': article.title,
                'text': article.text
            }
            resp["vector"] = vector
            return resp
        except Exception as e:
            print(f"[EXCEPTION] {e}")
            return None
        
    def get_article_by_url(self, url):
        try:
            article = self.google_news.get_full_article(url) 
            return article
        except:
            return None
    
    def get_articles(self, resps):
        articles = []
        print("Reading articles:")
        for i, resp in enumerate(resps):
            # print(f"{i+1}) {resp["title"]}")
            article = self.get_article(resp)
            if article: articles.append(article)
        return articles
    
    def scrape_for_query(self, query):
        # print(f"Looking up articles relating [ {query} ] ...")
        resps = self.get_query_response(query)
        # print(f"{len(resps)} matches")
        return self.get_articles(resps)
    
    def _convert_date_format(self, date_str):
        # Parse the date string into a datetime object
        dt = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z")
        # Format the datetime object into the desired format, excluding time
        formatted_date = dt.strftime("%Y-%m-%d")
        return formatted_date

        


def write_json_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except:
        return False

if __name__ == '__main__':
    print("Launching...")
    scraper = Scraper(max_results=10, start_date=(2022, 5, 1), end_date=(2022, 5, 20))
    query = "Five migrants found dead off the coast of Tunisia"
    res = scraper.scrape_for_query(query)
    write_json_to_file(res, f"../data/{query}.json")
    print(f"Saved query results in data/{query}.json")
    print("DONE")


