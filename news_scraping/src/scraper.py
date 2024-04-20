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
        for resp in resps:
            article = self.get_article(resp)
            if article: articles.append(article)
        return articles
    
    def scrape_for_query(self, query):
        resps = self.get_query_response(query)
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
    scraper = Scraper(max_results=5, start_date=(2022, 5, 1), end_date=(2022, 5, 20))
    print(scraper.google_news.period)
    query = "Several migrants feared dead off coast of Spain's Canary Islands"
    res = scraper.scrape_for_query(query)
    write_json_to_file(res, "../data/test2.json")
    print("DONE")


