import openai
from openai import OpenAI


class DocumentSimilarity:
    def __init__(self, client):
        self.client = client

    def check_document_coherence(self, doc1, doc2):
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are to analyze the coherence between two documents."},
                {"role": "user", "content": f"Document 1: {doc1}"},
                {"role": "user", "content": f"Document 2: {doc2}"},
                {"role": "user", "content": "Are these two documents discussing the same specific event related to migrant disappearances or deaths? Please analyze and describe any similarities or differences in the events, dates, locations, and involved parties mentioned in each document. If the answer is Yes say only yes otw say only No"}
            ]
        )
        return response.choices[0].message.content


    def check_list_documents(self, doc, docs):
        list_y_docs=[]
        list_n_docs=[]
        for d in docs:
            response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are to analyze the coherence between two documents."},
                {"role": "user", "content": f"Document 1: {doc}"},
                {"role": "user", "content": f"Document 2: {d}"},
                {"role": "user", "content": "Are these two documents discussing the same specific event related to migrant disappearances or deaths? Please analyze and describe any similarities or differences in the events, dates, locations, and involved parties mentioned in each document. If the answer is Yes say only yes otw say only No"}
            ]
        )
            if response.choices[0].message.content == "Yes":
                list_y_docs.append(d)
            else:
                list_n_docs.append(d)
        
        return list_y_docs, list_n_docs