import requests
import json
url = 'http://192.168.52.3/translate'
# url = 'http://localhost:8080/translate'
# url2 = 'http://152.136.232.202/mercube/translate'

translate_text = '''"There was nothing casual about this," Yates said in an interview with CNN's Anderson Cooper, reacting to White House press secretary Sean Spicer's assertion that her warning about Flynn's interactions with Russian representatives was a "heads up."
"I absolutely did not use the term heads up," Yates told Cooper. "I called (White House counsel) Don McGahn and told him I had a very sensitive matter I need to discuss with him that day in person."''','''"I absolutely did not use the term heads up," Yates told Cooper. "I called (White House counsel) Don McGahn and told him I had a very sensitive matter I need to discuss with him that day in person."
The exclusive interview, which aired in its entirety Tuesday evening, was Yates' first on television since being fired by President Donald Trump. It was taped on Monday morning, prior to an explosive report by The New York Times that Trump had asked ousted FBI Director James Comey to end the investigation into Flynn.''','''Earlier this month, Yates testified in front of the Senate Judiciary Committee's Subcommittee on Crime and Terrorism regarding the Trump campaign's alleged ties to Russia, particularly Flynn's contact with Russian Ambassador to the US Sergey Kislyak.
Prior to Trump taking office, Flynn had discussed sanctions with the official.'''
parameters = {
    "srcl":"nen", # 原文 英文
    "tgtl":"nzh", #  目标 中文 # string 或者 array
    # "text":["<p>There have now been more than 450 reports of severe lung problems</p>"],
    "text":" why you hurt me  so seriously? can you tell me the truth"

    # "app_source":3003,
    # "detoken":True
}

req = requests.post(url,data = json.dumps(parameters))
with open("origin.json",'w',encoding="utf-8")as f:
    f.write(req.text)

result = json.loads(req.text)
with open("test.json",'w',encoding="utf-8")as f:
    json.dump(result,f,ensure_ascii=False)
# translation = result['translation']['translated']['text'][0]
# print(translation)