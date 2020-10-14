from flask import Flask,render_template, request, request, url_for, session
import requests
import json
import random

app_id = '46f8fc36'
app_key = '43adc50a2f3ba559f46f7ab46176eed1'

language = 'en-gb'
#word_id = 'prone'
fields = 'definitions'
strictMatch = 'false'
words={'word1':[],'word2':[],'word3':[],'word4':[],'word5':[],'word6':[],'word7':[],'word8':[],'word9':[],'word10':[]}
W1 = 0 
W2 = 0 
W3 = 0 
W4 = 0 
W5 = 0 
W6 = 0 
W7 = 0 
W8 = 0 
W9 = 0 
W10 = 0 
M1 = 0 
M2 = 0 
M3 = 0 
M4 = 0 
M5 = 0 
M6 = 0 
M7 = 0 
M8 = 0 
M9 = 0 
M10 = 0 
Ws=[W1, W2, W3, W4, W5, W6, W7, W8, W9, W10]
Ms=[M1, M2, M3, M4, M5, M6, M7, M8, M9, M10]

app=Flask(__name__)
app.secret_key="heythere"



#=========================================== Function definitions ===============================================



def getWord():
    wordList=[]
    with open("dict.txt",'r') as file:

        for line in file:
            word = line.strip()
            wordList.append(word)
    wordList = wordList
    
    num=len(wordList)
    randnum=num*random.random()
    randnum=int(randnum)
    print(randnum)
    randWord=wordList[(randnum-1)]
    word_id= randWord
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    answer=r.text
    rescode=str(r.status_code).strip()
    print(rescode)
    if rescode=='200':
        res = json.loads(answer)
        print(word_id)
        try:
            res=res["results"][0]["lexicalEntries"][0]['entries'][0]['senses'][0]['definitions'][0]
            print(randWord,res)
            wM=[randWord,res]
            return wM
        except:
            return getWord()
    else:
        return getWord()






def genTenWords():
    for w in words:
        new=getWord()
        print(type(new))
        words[w]=new
        
    
    
    return words


#=========================================== Before webapp function calls =====================================

genTenWords()

for w in words:
    print(words[w])   
    # 
    # 
    # 
print(len(words)) 
n=0
for w in words:
    Ws[n]=words[w][0]
    Ms[n]=words[w][1]
    n+=1






#============================================Flask webapp stars here =========================================================

@app.route("/")
def home():
    return render_template("index.html",W1 = Ws[0], W2 = Ws[1], W3 = Ws[2], W4 = Ws[3], W5 = Ws[4], W6 = Ws[5], W7 = Ws[6], W8 = Ws[7], W9 = Ws[8], W10 = Ws[9], M1 = Ms[0], M2 = Ms[1], M3 = Ms[2], M4 = Ms[3], M5 = Ms[4], M6 = Ms[5], M7 = Ms[6], M8 = Ms[7], M9 = Ms[8], M10 = Ms[9])
    





if __name__=='__main__':
    app.run(debug=True)










#================================================Test Commands====================================================


