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
تخطي الروابط
انتقل الى المحتوى
Navigation menu
أخبار
الآن
اعرض المزيد
اقتصاد
ثقافة
رياضة
تكنولوجيا
مقالات
صحة
فيديو
المزيد
اعرض المزيد
البث الحي
اضغط هنا للبحث
تسجيل الدخول
أخبار
ارتفاع قتلى غرق قارب قبالة سواحل إيطاليا وروما تطالب بوقف قوارب الهجرة

Rescuers recover a body at a beach near Cutro, southern Italy, after a migrant boat broke apart in rough seas, Sunday, Feb. 26, 2023. Rescue officials say an undetermined number of migrants have died and dozens have been rescued after their boat broke apart off southern Italy. (AP Photo/Giuseppe Pipita)
مدة الفيديو 02 minutes 47 seconds
02:47
28/2/2023
احفظ المقالات لقراءتها لاحقا وأنشئ قائمة قراءتك

انتشل رجال الإنقاذ 4 جثث أخرى بعد يوم من غرق قارب خشبي كان يقل مهاجرين غير نظاميين إلى أوروبا إثر اصطدامه بالصخور، وسط طقس عاصف قبالة شاطئ إيطاليا فجر الأحد الماضي، ليرتفع عدد القتلى إلى 63، بينهم 14 طفلا. من جانبها، قالت رئيسة الوزراء الإيطالية جورجيا ميلوني -في مقابلة تلفزيونية- إنها بعثت رسالة إلى قادة الاتحاد الأوروبي تدعو فيها التكتل إلى اتخاذ إجراء فوري لوقف رحلات المهاجرين بالقوارب إلى أوروبا لمنع المزيد من الوفيات.

وأجرى خفر السواحل الإيطالي أمس الاثنين عملية بحث في البحر والشواطئ عن جثث خلفها تحطّم مركب قبالة كالابريا، في حين تحاول السلطات تحديد هويات القتلى، في ظل انتقادات لسياسة الحكومة الإيطالية بشأن الهجرة.

وقال منقذون إن معظم المهاجرين قدموا من أفغانستان، إضافة إلى إيران والصومال وسوريا وأماكن أخرى. وقالت وزارة الخارجية في إسلام آباد إن 20 باكستانيا كانوا على متن القارب، وفقد منهم 4 ونجا 16 آخرون.

وجرفت المياه كثيرا من الضحايا إلى الشاطئ قبالة موقع غرق القارب قرب منتجع ستيكاتو دي كوترو على الساحل الشرقي لكالابريا، وانتشلت بعض الجثث من البحر الذي بدأت أمواجه تهدأ مع تراجع قوة الرياح العاصفة.

People pray for the shipwreck victims in Italy People pray for the shipwreck victims in Italy- - CROTONE, ITALY - FEBRUARY 27: People pray outside PalaMilone Sports Hall, where victims' coffins are kept in the aftermath of a migrant shipwreck occurred in Steccato di Cutro, in Crotone, Italy on February 27, 2023. Some 200 people were on board vessel that sank off southern Calabria region's coast. DATE 28/02/2023 SIZE x SOURCE Anadolu/Valeria Ferraro
بعض السكان وضعوا الزهور والشموع عند سور معدني خارج قاعة جمعت فيها النعوش لتأبين الضحايا (الأناضول)
تأبين الضحايا
ووُضعت عشرات النعوش في قاعة رياضية ببلدة كروتوني المجاورة استعدادا لإقامة جنازة، في حين وضع بعض السكان الزهور والشموع عند سور معدني بالخارج لتأبين الضحايا.

وأمَّ الصلاة على الضحايا إمام مسلم، كما جاء أسقف كاثوليكي للصلاة وتقديم التعازي، في حين جلس بعض الناجين يبكون خارج الصالة الرياضية وسط جو بارد.

وقالت السلطات المحلية إن 81 شخصا نجوا من الحادث، لكن يُعتقد أن القارب كان يقل ما يتراوح بين 180 و200 شخص عندما أبحر من إزمير (غربي تركيا)، مما يرجح أن كثيرين ربما لقوا حتفهم أو ما زالوا مفقودين.

وأشار سرجيو دي داتو -الذي يقود فريقا من منظمة أطباء بلا حدود يقدّم الدعم النفسي للناجين- إلى وجود حالات لأطفال يتّمتهم الكارثة. وقال إن "طفلا أفغانيا يبلغ 12 عاما فقد عائلته بأكملها المكوّنة من 9 أفراد؛ هم أشقاؤه الأربعة ووالداه وأقارب مقرّبون جدا".

وذكرت تقارير إعلامية أمس الاثنين أنه تم توقيف 3 بشبهة تهريب البشر، وتبحث الشرطة عن شخص رابع.

وأجج الحادث مرة أخرى الجدل حول الهجرة في أوروبا، وكذلك في إيطاليا، حيث أثارت القوانين الجديدة الصارمة لحكومتها اليمينية حديثا بشأن عمل المنظمات الخيرية المعنية بإنقاذ المهاجرين انتقادات من الأمم المتحدة وجهات أخرى.

وقال مدير برامج أطباء بلا حدود في إيطاليا ماركو بيرتوتو "هذه الحوادث المفجعة تأتي نتيجة التبعات المأسوية للسياسات الإيطالية والأوروبية وحماية الحدود والحد من المرور الآمن والمنتظم إلى أوروبا".

Italian Prime Minister Meloni Visits Berlin
جورجيا ميلوني بعثت رسالة لقادة الاتحاد الأوروبي تدعوهم إلى اتخاذ إجراء فوري لوقف رحلات المهاجرين بالقوارب (غيتي)
موقف إيطالي
وفي حديثها مع تلفزيون "آر إيه آي" (RAI) العام، قالت رئيسة الوزراء الإيطالية "كلما غادر عدد أكبر من الناس زاد خطر الموت. الطريقة الوحيدة لمعالجة هذه القضية بجدية وبإنسانية هي وقف المغادرة".

وتعهدت ميلوني -التي انتُخبت في سبتمبر/أيلول الماضي- بوضع حد لوصول المهاجرين، وأكدت أن الحكومة "ملتزمة بمنع مغادرة (قوارب الهجرة) وما يترافق مع ذلك من المآسي".

في غضون ذلك، أثار وزير الداخلية ماتيو بيانتيدوزي انتقادات واسعة النطاق بعد أن ألقى اللوم على مهربي البشر والمهاجرين في الشروع في رحلات بحرية خطيرة مع عائلاتهم.

وقال للصحفيين "اليأس لا يمكن أبدا أن يكون سببا للسفر في ظروف تعرض حياة أطفالهم للخطر".

ووصل مئات الآلاف من المهاجرين إلى إيطاليا بالقوارب خلال العقد الماضي فارين من الصراعات وشظف العيش في بلادهم.

وسجل مشروع المهاجرين المفقودين التابع للأمم المتحدة أكثر من 20 ألف وفاة واختفاء في عرض البحر المتوسط منذ عام 2014، بما في ذلك أكثر من 220 هذا العام، مما يجعله أخطر طريق للهجرة في العالم.

المصدر : الجزيرة + وكالات
حول هذه القصة
تسلسل زمني منذ 2015.. البحر المتوسط يلتهم آلاف المهاجرين
بعد غرق عشرات المهاجرين قبالة سواحل جنوب إيطاليا أمس الأحد، يكون البحر المتوسط قد تسبب في وفاة واختفاء أكثر من 20 ألف مهاجر منذ عام 2015، ونسرد هنا تسلسلا زمنيا لبعض أسوأ حوادث تحطم القوارب بالمنطقة.


مدة الفيديو 02 minutes 47 seconds
02:47
مصرع عشرات المهاجرين بعد غرق مركبهم قبالة سواحل إيطاليا ومشاهد مأساوية على الشاطئ
ارتفع عدد غرقى مركب يحمل مهاجرين غير نظاميين قبالة سواحل إيطاليا إلى 59 بمنطقة كالابريا، وإثر الحادثة تعهدت رئيسة الوزراء الإيطالية جورجيا مليوني بالتصدي للهجرة غير النظامية.

Rescuers recover a body after a migrant boat broke apart in rough seas, at a beach near Cutro, southern Italy, Sunday, Feb. 26, 2023. Rescue officials say an undetermined number of migrants have died and dozens have been rescued after their boat broke apart off southern Italy. (AP Photo/Giuseppe Pipita)
شاهد.. تحقيق للجزيرة يكشف أدلة على عمليات إعادة قسرية غير قانونية لطالبي لجوء من إيطاليا إلى اليونان
كشف تحقيق أجرته الجزيرة بالتعاون مع منظمة لايت هاوس ريبورتس وشركاء إعلاميين، عن أدلة على عمليات إعادة القسرية غير قانونية لطالبي اللجوء، بمن فيهم القصّر، في ظروف غير إنسانية من إيطاليا إلى اليونان.


مدة الفيديو 04 minutes 43 seconds
04:43
اجتماع للاتحاد الأوروبي بشأن الهجرة بعد خلاف بين فرنسا وإيطاليا.. وبالصدفة صربيا تكتشف 600 مهاجر قرب حدودها
عقد وزراء داخلية الاتحاد الأوروبي الجمعة اجتماعا طارئا في محاولة لتخفيف التوتر المتصاعد بشأن الهجرة غير النظامية، خاصة بين فرنسا وإيطاليا، في حين اكتشفت صربيا بالصدفة 600 مهاجر قرب حدودها مع المجر.

Serbian police find migrants after shootout near Hungarian border
المزيد من أخبار العالم
الأمم المتحدة تحذر من خطر ظهور جبهة جديدة في دارفور
آثار الدمار جراء معارك بين مليشيات متصارعة في ريف الفاشر شمالي دارفور (مواقع التواصل-أرشيف)
مقتل مراسل صحفي روسي وأضرار بمنشآت تخزين الحبوب بميناء أوكراني
نيران جراء قصف روسي سابق على منطقة خاركيف الأوكرانية (أسوشيتد برس)
قتيل وأضرار بهجوم بابل والتحقيق يثبت غياب أي طائرات خلال الانفجار
الانفجار الذي وقع في بابل تسبب في وقوع خسائر مادية وإصابات (الفرنسية)
صورة بالأقمار الصناعية لقاعدة أصفهان الإيرانية بعد الهجوم الإسرائيلي
الصورة تظهر الأضرار التي لحقت برادار بطارية الدفاع الجوي روسية الصنع (مواقع التواصل)
يتصدر الآن
الحرب على غزة.. غارات على مناطق بالقطاع والاحتلال يواصل اقتحام مخيم طولكرم لليوم الثاني
البث الحي (الجزيرة)
نيوزويك: بعد 6 أشهر حماس تسيطر على الوضع في غزة
كاتز: السبب وراء تحدي حماس المذهل لكل معايير النصر والهزيمة هو ببساطة أنها المنتصرة حتى الآن (الجزيرة)
هآرتس: دول عربية دعمت إسرائيل تواجه صعوبة في تبرير موقفها لشعوبها
إيران أطلقت عشرات المسيّرات والصواريخ على إسرائيل (رويترز)
عدد الخطوات وحده لا يكفي.. إليك الطريقة المثلى لتمرين المشي المفيد
دراسة: تعزيز كثافة المشي تتعلق بتقوية القلب وتقليل معدلات انقطاع التنفس أثناء النوم والسكري وارتفاع ضغط الدم (بيكسلز)
من نحن
من نحن
الأحكام والشروط
سياسة الخصوصية
سياسة ملفات تعريف الارتباط
تفضيلات ملفات تعريف الارتباط
خريطة الموقع
تواصل معنا
تواصل معنا
احصل على المساعدة
أعلن معنا
رابط بديل
ترددات البث
بيانات صحفية
شبكتنا
مركز الجزيرة للدراسات
معهد الجزيرة للإعلام
تعلم العربية
مركز الجزيرة للحريات العامة وحقوق الإنسان
قنواتنا
الجزيرة الإخبارية
الجزيرة الإنجليزي
الجزيرة مباشر
الجزيرة الوثائقية
الجزيرة البلقان
عربي AJ+
تابع الجزيرة نت على:

شعار شبكة الجزيرة الإعلامية
جميع الحقوق محفوظة © 2024 شبكة الجزيرة الاعلامية

يمكنك الاعتماد على الجزيرة في مسألتي الحقيقة والشفافيةبحيث نضطلع نحن 823 وشركاؤنا بتخزين المعلومات والوصول إليها عبر جهازك، ومن ذلك على سبيل المثال المعرفات الفريدة في ملفات تعريف الارتباط لمعالجة البيانات الشخصية. يمكنك الموافقة على اختياراتك وإدارتها في أي وقت من خلال النقر على زر "إدارة التفضيلات"، ولا سيما الاحتفاظ بحقك في الاعتراض حيثما يتم الاستناد إلى المصلحة المشروعة. سيتم إبلاغ شركائنا على الصعيد العالمي باختياراتك، ولن يؤثر ذلك في عملية التصفح التي تجريها.لمعرفة مزيد من التفاصيل، يرجى الاطلاع على سياسة ملفات تعريف الارتباط الخاصة بنا.
نعالج، نحن وشركاؤنا، البيانات من أجل:
استخدام بيانات الموقع الجغرافي الدقيقة. فحص خصائص الجهاز بشكل فعال من أجل تحديد الهوية. تخزين المعلومات و/أو الوصول إليها على أحد الأجهزة. الإعلانات والمحتوى المخصصان وقياس أداء الإعلانات والمحتوى وأبحاث الجمهور وتطوير الخدمات.قائمة الشركاء (مقدّمو الخدمات)

السماح للكلّ
رفض الكلّ
إدارة التفضيلات
"""


api_key = "sk-proj-lUvpZCOU4TV1QUYTolbvT3BlbkFJPhadzOExwwSAWylFMHKC"
print(check_document_coherence(doc1, doc2, api_key))
