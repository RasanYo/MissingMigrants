import openai

class QueryGenerator:
    def __init__(self, open_ai_client):
        self.open_ai_client = open_ai_client

    def generate_queries(self, news_report):
        prompt = f"Given the news report: {news_report}, generate a list of queries to find similar news articles on Google News."
        response = self.open_ai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a journalist who wants to find similar news articles on Google News. Here is the news report: {news_report}"},
            {"role": "user", "content": f"{prompt}. What are some queries I can use to find similar news articles on Google News? Please return the information in JSON format. For example: {{'query1': 'query1_text', 'query2': 'query2_text'}}"},
        ],
        max_tokens=1000,
        response_format={"type": "json_object"}
        )
        return response.choices[0].message.content
        