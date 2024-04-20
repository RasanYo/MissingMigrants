import openai


class QueryGenerator:
    def __init__(self, open_ai_client):
        self.open_ai_client = open_ai_client

    def generate_queries(self, initial_search_query, languages, q_per_lang):
        prompt = f"""
        Given the search query: "{initial_search_query}", generate a list of alternative queries to maximize the retrieval of news articles on Google News related to this topic.
        Each query should be:
        - Related to the main topic but vary slightly to cover different angles or related subtopics.
        - Composed of 5-6 words to maintain focus and precision.
        - Suitable for use in various languages as specified.

        Please format the response as a JSON object with separate entries for each language in {languages}, containing {q_per_lang} queries each. For example, the JSON should look like this: {{'english': {{'1': 'query1_text', '2': 'query2_text'}}, 'spanish': {{'1': 'query1_es', '2': 'query2_es'}}}}.
        """

        response = self.open_ai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                "content": "You are a data analyst helping a journalism team to expand their search capabilities on Google News. Generate related search queries that explore different facets or perspectives of the initial query to ensure a comprehensive coverage of news."},
                {"role": "user",
                "content": prompt},
            ],
            max_tokens=1000,
            response_format={"type": "json_object"}
)
        return response.choices[0].message.content
