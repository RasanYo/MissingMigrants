import openai
import os
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import json

os.environ["OPENAI_API_KEY"] = "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"

TEMPLATE = """
Input News Article: {article}

Extract the relevant information from the news article.

Output the response in the given format below. It is possible to not find all the informations in the article, in which case you must pust 'Unknown' for the corresponding property.
Output:

Country of Incident: <string>
Region of Inciden: <string>
City of Incident: <string>
Incident Date: <Date: YYYY-MM-DD>
Number of Dead: <integer>
Minimum Estimated Number of Missing: <integer>
Total Number of Dead and Missing: <integer>
Number of Survivors	Number of Females: <integer>
Number of Males	Number of Children: <integer>
Country of Origin (of the people): [<string>]
Region of Origin (of the people): [<string>]
Cause of Death: <string>
Country of Incident: <string>
Migration Route: <string>
Location of Incident: <string>

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
    
    article = """On Monday, Tunisia's coastguard retrieved the bodies of five migrants, raising the week's death toll to 11. They also rescued a total of 663 migrants, reflecting a surge in crossings from North Africa to Italy due to improved weather.

The coastguard reported on Monday that five bodies were recovered near the coastal city of Sfax. In the past four days, a total of 11 migrants have been found dead in the area.

Tunisian security forces have also prevented 3,058 migrants from crossing to Europe by boat since Friday. The majority of them are said to have come from sub-Sahara Africa.

On Monday alone, 633 people were stopped from setting off by boat from Tunisia towards Europe following a rescue mission. Security forces also reportedly arrested 120 smugglers.

Additionally, a shipwreck off the Italian coast over the weekend likely resulted in the death of a 15-month-old girl.

Also read: 17 Tunisian migrants missing at sea as reported deaths reach record high

Oil tanker rescues refugees
In the early hours of Monday, an oil tanker in the Mediterranean Sea picked up 139 people from an unseaworthy vessel on their way to Europe from Libya, Italian authorities reported.

During the rescue operation, three migrants fell into the water and remain missing at sea. The initial search for them was unsuccessful, according to reports.

The rest of the rescued migrants were taken by the Italian coastguard to the Italian Mediterranean island of Lampedusa. The migrants were said to have originated from various African countries, as well as from Syria, Pakistan, and Bangladesh.

Lampedusa, situated between Sicily and Tunisia, has long been a focal point of the smuggling trade. Reports indicate that passengers paid between $3,000 and $7,000 for the dangerous journey on the 12-meter boat.

Also read: EU-Tunisia migration deal: Encouraging the people smugglers?

New agreements on migration and labor
Under a recent agreement signed between the Italian and Albanian governments, rescued migrants from the Mediterranean could soon increasingly be taken to Albania for processing -- instead of remaining at a reception center in Lampedusa before being transferred to the Italian mainland. Two reception centers and a repatriation center are scheduled to open in Albania in May to facilitate this process.

This comes after the EU reached a controversial agreement with Tunisia late last year: in exchange for millions of euros in financial aid, the North African country is expected to take stronger action against traffickers and illegal crossings. However, there have been doubts about the sustainability of this agreement.

Earlier this year, Italy and Tunisia also signed a deal to bring 12,000 Tunisian workers to Italy over the next three years. Under the deal, Italian and Tunisian labor organizations, Sviluppo Lavoro Italia and Aneti, will collaborate to identify the workforce requirements of the Italian market and the Tunisian workers who could meet those demands.

Also read: EU criticized over migration deal with Egypt

Fewer crossings compared to last year
According to the Tunisian Forum for Economic and Social Rights (FTDES), over 1,300 migrants attempting to cross to Europe from the coast of Tunisia were killed in 2023.

Compared to last year, the number of migrants arriving in Italy via the central Mediterranean route, mostly from Tunisia and Libya, has meanwhile decreased.

The Italian Interior Ministry counted nearly 9500 people reaching Italy by sea so far this year, compared to over 20,000 in the same period last year."""
    
    extractor = OpenAIInfoExtractor()
    response = {}
    while (len(response) != 16):
        response = extractor.run(article=article)
    print(response)