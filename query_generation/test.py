from query_generation import QueryGenerator
import os
from openai import OpenAI


os.environ["OPENAI_API_KEY"] = "sk-proj-xbow1HvGwTEa3Q6WWua7T3BlbkFJ0bVV4skXOfMDU38IESbB"


def main():
    open_ai_client = OpenAI()
    query_gen = QueryGenerator(open_ai_client)

    queries = query_gen.generate_queries("migrants found dead", ["english"], 2)
    print(queries)


if __name__ == "__main__":
    main()