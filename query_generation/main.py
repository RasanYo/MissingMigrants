from openai import OpenAI
from query_generation import QueryGenerator

def main():
    api_key = "sk-proj-lUvpZCOU4TV1QUYTolbvT3BlbkFJPhadzOExwwSAWylFMHKC"
    open_ai_client = OpenAI(api_key=api_key)

    query_gen = QueryGenerator(open_ai_client)
    query = query_gen.generate_queries("Migrants dead italy")

    print(f"Generated query: {query}")


if __name__ == "__main__":
    main()