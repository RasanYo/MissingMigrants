from query_generation import QueryGenerator
import os
from openai import OpenAI


os.environ["OPENAI_API_KEY"] = "your-api-key"


def main():
    open_ai_client = OpenAI()
    query_gen = QueryGenerator(open_ai_client)

    queries = query_gen.generate_queries("migrants found dead", ["english"], 2)
    print(queries)


if __name__ == "__main__":
    main()
