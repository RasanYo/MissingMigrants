from openai import OpenAI
from query_generation import QueryGenerator

def main():
    api_key = "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"
    open_ai_client = OpenAI(api_key=api_key)

    query_gen = QueryGenerator(open_ai_client)
    query = query_gen.generate_queries("Several migrants feared dead off coast of Spain's Canary Islands")

    print(f"Generated query: {query}")


if __name__ == "__main__":
    main()