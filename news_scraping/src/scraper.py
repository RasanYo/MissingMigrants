from gnews import GNews
import json

APIFY_API_KEY = 'apify_api_SsXrbMedr8qm11DLb7394OISl7kFAz0oKzMw'

class Scraper:
    
    def __init__(self, **kargs):
        self.google_news = GNews(**kargs)

    def set_gnews(self, gnews):
        self.google_news = gnews

    def get_query_response(self, query):
        return self.google_news.get_news(query) 


    def get_article(self, resp):
        try:
            article = self.google_news.get_full_article(resp['url']) 
            resp["article"] = {
                'title': article.title,
                'text': article.text
            }
            return resp
        except:
            return None
    
    def get_articles(self, resps):
        articles = []
        print("Reading articles:")
        for i, resp in enumerate(resps):
            print(f"{i+1}) {resp["title"]}")
            article = self.get_article(resp)
            if article: articles.append(article)
        return articles
    
    def scrape_for_query(self, query):
        print(f"Looking up articles relating [ {query} ] ...")
        resps = self.get_query_response(query)
        print(f"{len(resps)} matches")
        return self.get_articles(resps)
        


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
    query = "migrant canary islands missing"
    res = scraper.scrape_for_query(query)
    write_json_to_file(res, f"../data/{query}.json")
    print(f"Saved query results in data/{query}.json")
    print("DONE")


