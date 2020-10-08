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





#============================================Flask webapp stars here =========================================================

@app.route("/")
def home():
    return render_template("index.html", the_word1='Dani')
    





if __name__=='__main__':
    app.run(debug=True)










#================================================Test Commands====================================================

genTenWords()

for w in words:
    print(words[w])   
    # 
    # 
    # 
print(len(words)) 
