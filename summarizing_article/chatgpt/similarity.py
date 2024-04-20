import openai
from openai import OpenAI


def check_document_coherence(doc1, doc2, api_key):

    client = OpenAI(
    # This is the default and can be omitted
    api_key=api_key,
)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are to analyze the coherence between two documents."},
            {"role": "user", "content": f"Document 1: {doc1}"},
            {"role": "user", "content": f"Document 2: {doc2}"},
            {"role": "user", "content": "Are these two documents discussing the same specific event related to migrant disappearances or deaths? Please analyze and describe any similarities or differences in the events, dates, locations, and involved parties mentioned in each document. If the answer is Yes say only yes otw say only No"}
        ]
    )
    return response.choices[0].message.content

# Example usage
doc1 = """
Register
Sign In
Home
News
Sport
Business
Innovation
Culture
Travel
Earth
Video
Live
Italy migrant boat shipwreck: More than 100 people feared dead
28 February 2023
By Davide Ghiglione & Alexandra Fouché,
In Rome and in London
Share
0:25
Watch: Footage shows Italian emergency services helping survivors
There are fears more than 100 people, including children, have died after their boat sank off southern Italy.
At least 63 migrants are confirmed to have died, with 12 children including a baby said to be among the victims.
The vessel, thought to have carried some 200 people, broke apart while trying to land near Crotone on Sunday.
Italy's Prime Minister Giorgia Meloni has urged EU institutions to take action to stop clandestine migrant boat journeys.
On board the boat, which had set out from Turkey a few days earlier, were said to be people from Afghanistan, Pakistan, Somalia, Syria, Iraq, and Iran.
According to the Pakistani foreign ministry 16 of its citizens had survived the disaster, with four more missing.
The coastguard said 80 people had been found alive, 'including some who managed to reach the shore after the sinking', meaning many more remained unaccounted for.
One survivor was arrested on migrant trafficking charges, customs police said.
As bodies were recovered from the beach and assistance and relocation operations continued, a group of survivors of the deadly shipwreck struggled to come to terms with the loss of their loved ones.
At a temporary reception centre in the town of Isola di Capo Rizzuto, some of them were crying without speaking, some were just staring into the void, wrapped in blankets.
'They are heavily traumatised,' said Sergio Di Dato, from charity Médecins Sans Frontières. 'Some children have lost their whole family. We are offering them all the support we can.'
A 16-year-old boy from Afghanistan lost his 28-year-old sister, who died on the beach next to him. He could not find the strength to tell his parents.
A 43-year-old man from Afghanistan survived with his 14-year-old son, but his wife and his three other children, who were 13, nine, and five, did not make it. Another Afghan woman in tears would not move from the beach after losing her husband.
'This is yet another tragedy happening near our shores. It reminds us all that the Mediterranean is a giant mass grave, with tens of thousands of souls in it, and it continues to widen,' said Francesco Creazzo, from SOS Méditerranée, an non-governmental organisation engaged in rescue operations in the central Mediterranean.
'There is no end in sight; in 2013, people said 'never again' to the little white coffins of Lampedusa, in 2015, they said 'never again' in front of the lifeless body of a two-year-old Syrian child on a beach.
'Now the words 'never again' are not even pronounced any more. We only hear 'no more departures', but unfortunately people keep venturing on this journey and they keep dying,' he added.
EPA Crotone: Muslims saying prayers for the victims, 27 Feb 23EPA
Crotone: Muslims said prayers for the victims as a sea search continued
Speaking at the UN's Human Rights Council in Geneva on Monday morning, Secretary General António Guterres called on countries to do more to help refugees and migrants, and called for safer travel routes and strengthened rescue operations.
Prime Minister Meloni - elected last year partly on a pledge to stem the flow of migrants into Italy - on Monday said the only way to tackle the issue of migrant departures 'seriously' and 'with humanity' was to stop migrant boat journeys.
Speaking to Italian public broadcaster Rai 1, she said she had written to the European Council and European Commission calling for immediate action to stop migrant boat departures in order to prevent more deaths.
'The more people depart, the more risk dying,' she said.
Earlier on Sunday, she expressed 'deep sorrow' after the incident and blamed the deaths on people smugglers.
'It is inhumane to exchange the lives of men, women, and children for the price of the 'ticket' they paid in the false perspective of a safe journey,' she said.
'The government is committed to preventing departures, and with them the unfolding of these tragedies, and will continue to do so.'
Ms Meloni's right-wing government has vowed to stop migrants reaching Italy's shores and in the last few days pushed through a tough new law tightening the rules on rescues.
The vessel is reported to have sunk after it crashed against rocks during rough weather.
Video footage shows timber from the wreckage washing up on the beach, along with parts of the hull.
According to monitoring groups, more than 20,000 people have died or gone missing at sea in the central Mediterranean since 2014.
Graphic showing number of deaths in the Mediterranean since 2014
A map of the Mediterranean showing the location of Crotone on the Calabrian coast of Italy where the migrant boat was shipwrecked.
At least 59 migrants dead in shipwreck off Italy
At least 73 migrants lost after Libya shipwreck
Four people dead after migrant boat started sinking
Nearly 1,200 migrants arrive in Italy in 24 hours
Pakistan
Turkey
Afghanistan
Giorgia Meloni
Iran
Europe migrant crisis
Somalia
Italy
Iraq
Syria
Related
New Zealand in Pakistan 2024
4 days ago
Cricket
Lightning and rain kill dozens in Pakistan
4 days ago
Asia
At least 17 Pakistani pilgrims killed in Eid crash
11 Apr 2024
Asia
More
8 hrs ago
An Iranian woman walks past a huge anti-Israeli banner carrying pictures of missiles, in Tehran, Iran, 19 April 2024.
An audible sigh of relief in the Middle East
The latest round in the longstanding, dangerous rivalry between Israel and Iran seems over for now, Lyse Doucet writes.
Middle East
10 hrs ago
Photo posted by Iraqi news outlet Sabereen News on Telegram reportedly showing remains of an Israeli missile in central Iraq
What we know about Israel's missile attack on Iran
There are competing claims about the scale of Friday's attack on the Isfahan region.
Middle East
15 hrs ago
Merlyn Thomas and footage from Israel's attack on Iran
BBC Verify examines video from Israel's attack on Iran
Footage showing explosions in the sky over Iran has been analysed by BBC Verify.
Middle East
16 hrs ago
A gas flare on an oil production platform is seen alongside an Iranian flag.
Oil price eases as Iran downplays attack
Oil prices eased after Iran said a missile strike from Israel did little damage.
Middle East
17 hrs ago
Katherine Miles with her family in Wadi Rum during their holiday
Family 'unnerved' after seeing Iranian missile attack
A Cambridge family paid almost £4,000 to get home from Jordan after their flight was cancelled.
Cambridgeshire
Home
News
Sport
Business
Innovation
Culture
Travel
Earth
Video
Live
Audio
Weather
BBC Shop
BBC in other languages
Terms of Use
About the BBC
Privacy Policy
Cookies
Accessibility Help
Contact the BBC
Advertise with us
Do not share or sell my info
Contact technical support
Copyright 2024 BBC. All rights reserved.  The BBC is not responsible for the content of external sites. Read about our approach to external linking.
"""
doc2 = """
Exclusive news, data and analytics for financial market professionals
Reuters home
World
Business
Markets
Sustainability
Legal
Breakingviews
More
My View
Sign In
Register
Europe
Migrant shipwreck in Italy kills at least 59, including 12 children
By Gianni, Daniele and Alvise Armellini
February 27, 20237:02 AM GMT+1Updated a year ago
ROME, Feb 26 (Reuters) - At least 59 people died, including 12 children, when a wooden sailing boat carrying migrants to Europe crashed against rocks near the southern Italian coast early on Sunday, authorities said.
The vessel, which sailed from Turkey and was carrying people from Afghanistan, Iran and several other countries, sank in rough seas before dawn near Steccato di Cutro, a seaside resort on the eastern coast of Calabria.
Advertisement · Scroll to continue
The incident reopened a debate on migration in Europe and Italy, where the recently-elected right-wing government's tough new laws for migrant rescue charities have drawn criticism from the United Nations and others.
Manuela Curra, a provincial government official, told Reuters that 81 people had survived the shipwreck. Twenty of them were hospitalized, including one person in intensive care.
Interior Minister Matteo Piantedosi, who travelled to the scene, said 20-30 people might still be missing, amid reports from survivors that the boat had been carrying between 150 to 200 migrants.
Advertisement · Scroll to continue
The vessel set sail from the western Turkish port of Izmir about four days ago and was spotted about 74 km (46 miles) off the Italian coast late on Saturday by a plane operated by European Union border agency Frontex, Italian police said.
Patrol boats were sent to intercept it, but severe weather forced them to return to port, police said, adding that authorities then mobilized search units along the coastline.
Advertisement · Scroll to continue
A baby aged only a few months was among those found washed up on the beach, ANSA news agency said.
Emergency doctor Laura De Paoli described finding another dead child, aged seven.
'When we got to the point of the shipwreck we saw corpses floating everywhere and we rescued two men who were holding up a child. Sadly, the little one was dead,' she told ANSA.
His voice cracking with emotion, Cutro's mayor, Antonio Ceraso, told the SkyTG24 news channel that he had seen 'a spectacle that you would never want to see in your life ... a gruesome sight ... that stays with you for all your life'.
Wreckage from the wooden gulet, a Turkish sailing boat, was strewn across a large stretch of coast.
One survivor was arrested on migrant trafficking charges, the Guardia di Finanza customs police said.
Bodies wash ashore in a suspected migrant shipwreck, in Cutro
Item 1 of 14 Rescuers recover a body after a suspected migrant boat is wrecked and bodies believed to be of refugees were found in Cutro, the eastern coast of Italy's Calabria region, Italy, February 26, 2023. REUTERS/Giuseppe Pipita
[1/14]Rescuers recover a body after a suspected migrant boat is wrecked and bodies believed to be of refugees were found in Cutro, the eastern coast of Italy's Calabria region, Italy, February 26, 2023. REUTERS/Giuseppe Pipita Purchase Licensing Rights, opens new tab
'FALSE PROSPECT' OF SAFETY
Italian Prime Minister Giorgia Meloni expressed deep sorrow for the deaths, and blamed human traffickers who profit while offering migrants 'the false prospect of a safe journey'.
'The government is committed to preventing departures, and with them the unfolding of these tragedies, and will continue to do so, first of all by calling for maximum cooperation from the countries of departure and of origin,' she said.
Meloni's administration has said migrant rescue charities are encouraging migrants to make the dangerous sea journey to Italy, and sometimes work in partnership with traffickers.
Charities strongly reject both accusations.
'Stopping, blocking and hindering the work of NGOs (non-governmental organisations) will have only one effect: the death of vulnerable people left without help,' Spanish migrant rescue charity Open Arms tweeted in reaction to Sunday's shipwreck.
However, the coast off Calabria has not been patrolled by NGO ships, which operate in the waters south of Sicily. That suggests they would have been unlikely to intercept the shipwrecked migrants regardless of Meloni's crackdown.
The head of the Italian Catholic Church, Cardinal Matteo Zuppi, called for the resumption of an EU search and rescue mission in the Mediterranean, as part of a 'structural, shared and humanitarian response' to the migration crisis.
A spokesman for the United Nations' International Organization for Migration (IOM), in the same vein, appealed on Twitter for the strengthening of rescue operations in the Mediterranean.
Flavio Di Giacomo also called for the opening of 'more regular migration channels' to Europe, and action to address what he said were the multiple causes pushing people to try the sea crossings.
Earlier on Sunday, Pope Francis, the son of Italian migrants to Argentina and long a vocal advocate for migrants' rights, said he was praying for the shipwreck's victims.
Italy is one of the main landing points for migrants trying to enter Europe by sea, with many seeking to travel on to richer northern European nations. But to do so, they must brave the world's most dangerous migration route.
The United Nations Missing Migrants Project, opens new tab has registered more than 20,000 deaths and disappearances in the central Mediterranean since 2014. More than 220 have died or disappeared this year, it estimates.
Coming soon: Get the latest news and expert analysis about the state of the global economy with Reuters Econ World. Sign up here.
Reporting from Rome by Alvise Armellini, Giselda Vagnoni, Angelo Amante, Crispian Balmer; Writing by Alvise Armellini Editing by Tomasz Janowski, Crispian Balmer, Barbara Lewis and Frances Kerry
Our Standards: The Thomson Reuters Trust Principles., opens new tab
"""

api_key = "sk-proj-7kEwFmHZ1El2NHJp5lRwT3BlbkFJH7B0H2VTBMEoZ68Kmi7r"
print(check_document_coherence(doc1, doc2, api_key))
