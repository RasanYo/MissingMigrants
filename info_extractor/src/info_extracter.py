import openai
import os
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import json

os.environ["OPENAI_API_KEY"] = "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"

TEMPLATE = """
Input News Article: {article}

Extract from the news article information and output it in the following order.
Note that it is possible to not find all informations in the article, so output Unknown for these informations

Output:
Region of Incident	
Incident Date	
Number of Dead	
Minimum Estimated Number of Missing	
Total Number of Dead and Missing	
Number of Survivors	Number of Females	
Number of Males	Number of Children	
Country of Origin (of the people)	
Region of Origin (of the people)
Cause of Death	
Country of Incident	
Migration Route	
Location of Incident
"""

class OpenAIInfoExtractor:
    def __init__(self):
        self.prompt = PromptTemplate(input_variables=['article'], template=TEMPLATE)
        self.llm_chain = LLMChain(llm=OpenAI(), prompt=self.prompt)
        
    def read_article(self, article):
        return self.llm_chain.run({'article': article})
     
    def llm_response_to_json(self, response):
        data_lines = response.strip().split('\n')
        response_dict = {}

        for line in data_lines:
            key, value = line.split(':')
            key = key.strip()
            value = value.strip()

            # Convert numerical values to integers if applicable
            if value.isdigit():
                value = int(value)
            elif value == 'Unknown':  # Handle 'Unknown' as a special value, or convert it to None or keep as string
                value = None

            # Assign the cleaned key and value to the dictionary
            response_dict[key] = value

        # Convert dictionary to JSON string if needed
        return response_dict
        
    def run(self, article):
        response = self.read_article(article)
        json_response = self.llm_response_to_json(response)
        return json_response
    
if __name__ == '__main__':
    article = """
    ‼️TRAGEDIE ‼️Le bateau qui a quitté Tan Tan avec 59 personnes (14 femmes et 6 enfants) il y a quelques jours a été secouru par la marine marocaine. 
    👉🏿46 survivants (10 femmes et 2 enfants) 
    👉🏿11 disparues 
    👉🏿2 corps trouvés 
    Paix à leurs âmes et condoléances aux familles"""
    
    extractor = OpenAIInfoExtractor()
    print(extractor.run(article=article))