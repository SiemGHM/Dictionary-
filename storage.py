#API request and reply


import requests
import json


app_id = '46f8fc36'
app_key = '43adc50a2f3ba559f46f7ab46176eed1'

language = 'en-gb'
word_id = 'prone'
fields = 'definitions'
strictMatch = 'false'

url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
#print("json \n" + json.dumps(r.json()))

answer=r.text

# using json.loads() 
# convert dictionary string to dictionary 
res = json.loads(answer)


#print(answers["results"])

#print(type(res))

print(res["results"][0]["lexicalEntries"][0]['entries'][0]['senses'][0]['definitions'][0])


