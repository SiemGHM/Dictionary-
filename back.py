from flask import Flask,render_template, request, request, url_for, session
import pymysql
import requests
import json
import random

app_id = '46f8fc36'
app_key = '43adc50a2f3ba559f46f7ab46176eed1'

language = 'en-gb'
#word_id = 'prone'
fields = 'definitions'
fields2 = 'pronunciations'
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
WC1 = 0 
WC2 = 0 
WC3 = 0 
WC4 = 0 
WC5 = 0 
WC6 = 0 
WC7 = 0 
WC8 = 0 
WC9 = 0 
WC10 = 0
P1 = 0 
P2 = 0 
P3 = 0 
P4 = 0 
P5 = 0 
P6 = 0 
P7 = 0 
P8 = 0 
P9 = 0 
P10 = 0  
Ws=[W1, W2, W3, W4, W5, W6, W7, W8, W9, W10]
Ms=[M1, M2, M3, M4, M5, M6, M7, M8, M9, M10]
WC=[WC1,WC2,WC3,WC4,WC5,WC6,WC7,WC8,WC9,WC10]
P=[P1 ,P2 ,P3 ,P4 ,P5 ,P6 ,P7 ,P8 ,P9 ,P10]



def mysqlcon(query):
    conn = pymysql.connect( 
        host='localhost', 
        user='SiemGHM',  
        password = "$iemGH12", 
        db='dexdb',
        autocommit=True 
        )

    cur = conn.cursor() 
    cur.execute(query) 
    output = cur.fetchall() 
    return output 
      
    # To close the connection 
    conn.commit()
    conn.close()

def dictDB(word):
    query = "select word, Meaning, WordCat, wordPro, def_res, pro_res from word where word='{}'".format(word)
    conn = pymysql.connect( 
        host='localhost', 
        user='SiemGHM',  
        password = "$iemGH12", 
        db='dexdb',
        autocommit=True 
        )

    cur = conn.cursor() 
    cur.execute(query) 
    output = cur.fetchall() 
    conn.close()
    return output



wordList=[]
with open("dict.txt",'r') as file:

    for line in file:
        word = line.strip()
        wordList.append(word)

# print(wordList)


app=Flask(__name__)
app.secret_key="heythere"



#=========================================== Function definitions ===============================================



def getWord():


        
    
    
    num=len(wordList)
    randnum=num*random.random()
    randnum=int(randnum)
    print(randnum)
    randWord=wordList[(randnum-1)]
    wordM = dictDB(randWord)
    if wordM:
        word = wordM[0][0]
        resp = wordM[0][1]
        wc = wordM[0][2]
        prn = wordM[0][3]
        wM=[word,resp,wc,prn]
        return wM

    word_id= randWord
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;
    
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    
    answer=r.text
    
    rescode=int(str(r.status_code).strip())
    res = json.loads(answer)
    print(res)
    
    
    
    #print(answer2)
    url2 = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields2 + '&strictMatch=' + strictMatch;
    r2 = requests.get(url2, headers = {'app_id': app_id, 'app_key': app_key})
    answer2=r2.text
    rescode2=int(str(r2.status_code).strip())
    res2=json.loads(answer2)
    sumrescode=(rescode+rescode2)
    print(sumrescode)
    
    
    if sumrescode==400:
        print('1')
        
        
        print(word_id)
        
        
        #print(answer2)
        print('2')
        try:
            resp=res["results"][0]["lexicalEntries"][0]['entries'][0]['senses'][0]['definitions'][0]
            print('4')
            WordC=res["results"][0]["lexicalEntries"][0]['lexicalCategory']['text']
            pron=res2["results"][0]["lexicalEntries"][0]['entries'][0]['pronunciations'][0]['phoneticSpelling']
            print("5")
            randWord = res["results"][0]["word"]
            #print(randWord,resp, WordC,pron)
            wM=[randWord,resp,WordC,pron]
            print('3')
            query = "insert into word (word, Meaning, WordCat, wordPro, def_res, pro_res) values ('{}','{}','{}','{}','{}','{}')".format(randWord, resp, WordC, pron, json.dumps(res),pron)
            #query = query.replace("'", "''")
            print(query)
            out = mysqlcon(query)
            print(out)

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
    WC[n]=words[w][2]
    P[n]=words[w][3]
    
    n+=1






#============================================Flask webapp stars here =========================================================

@app.route("/")
def home():
    return render_template("index.html",W1 = Ws[0], W2 = Ws[1], W3 = Ws[2], W4 = Ws[3], W5 = Ws[4], W6 = Ws[5], W7 = Ws[6], W8 = Ws[7], W9 = Ws[8], W10 = Ws[9], M1 = Ms[0], M2 = Ms[1], M3 = Ms[2], M4 = Ms[3], M5 = Ms[4], M6 = Ms[5], M7 = Ms[6], M8 = Ms[7], M9 = Ms[8], M10 = Ms[9],WC1 = WC[0], WC2 = WC[1], WC3 = WC[2], WC4 = WC[3], WC5 = WC[4], WC6 = WC[5], WC7 = WC[6], WC8 = WC[7], WC9 = WC[8], WC10 = WC[9], P1  = P[0], P2  = P[1], P3  = P[2], P4  = P[3], P5  = P[4], P6  = P[5], P7  = P[6], P8  = P[7], P9  = P[8], P10  = P[9])
    

@app.route('/IPA')
def ipa():
    return render_template("IPA.html")

@app.route('/lookup')
def lookup():
    return render_template("lu.html")

@app.route('/lookupr', methods=['POST','GET'])
def lookupr():
    word = request.form['myCountry']
    fields = 'definitions'
    fields2 = 'pronunciations'
    strictMatch = 'false'

    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;
    
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    
    answer=r.text
    
    rescode=int(str(r.status_code).strip())
    res = json.loads(answer)

    if rescode != 404:
        return render_template("lur.html", response = res["results"][0]["lexicalEntries"][0]['entries'][0]['senses'][0]['definitions'],res=res)
    else:
        return render_template("lur.html")



if __name__=='__main__':
    app.run(debug=True)










#================================================Test Commands====================================================


