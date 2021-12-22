from flask import Flask,render_template, request, request, url_for, session, jsonify, make_response, redirect 
from flask_login import logout_user
import pymysql
import requests
import json
import random
import time
import api
import schedule
import time


app_id = api.apiid
app_key = api.key

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

dbhost= 'dexdb.cp2yhiiajs4r.us-east-2.rds.amazonaws.com'


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
    query = "select word, Meaning, WordCat, wordPro from word where word='{}'".format(word)
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


def signupdb(name, lname, username, email, password, level):
    query = "insert into users (username,email, passwd) values ('{}','{}','{}')".format(username, email, password)
    ex = mysqlcon(query)
    uID = mysqlcon("select UserID from users where username='{}'".format(username))
    query = "insert into Customers (UserID, fname, lname, lvl) values ({},'{}','{}', '{}')".format(int(uID[0][0]),name, lname, level)
    ex = mysqlcon(query)


def lncheck(email,password):
    pw = mysqlcon("select passwd, username from users where email='{}'".format(email))
    print(pw)
    
    if pw:
        if password == pw[0][0]:
            return [True, pw[0][1]]
        else:
            return False
    else:
        return False



# wordList=[]
# with open("dict.txt",'r') as file:

#     for line in file:
#         word = line.strip()
#         wordList.append(word)

# print(wordList)


application = app=Flask(__name__)
app.secret_key="9dddnJbLcF44kyQx2KTT0w"





#=========================================== Function definitions ===============================================



def getWord(wordin = None):


    c=  time.time()
    
    
    # num=len(wordList)
    # randnum=num*random.random()
    # randnum=int(randnum)
    if wordin:
        word_id = wordin
    else:
        rw = "SELECT word FROM wlist AS t1 JOIN (SELECT wlid FROM wlist ORDER BY RAND() LIMIT 1) as t2 ON t1.wlid=t2.wlid"

        word_id = mysqlcon(rw)
        word_id=word_id[0][0]


    wordM = dictDB(word_id)
    if wordM:
        dbi = time.time()
        print("""we are actualy using the database ############################################################################################################################
        ###########################################################################################
        # #########
        # ##############
        # ############""")
        word = wordM[0][0]
        resp = wordM[0][1]
        wc = wordM[0][2]
        prn = wordM[0][3]
        wM=[word,resp,wc,prn]
        tbf = time.time()
        print(tbf-dbi)
        print(tbf-c, "This is the real shit")
        return wM

    
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;
    
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    
    answer=r.text
    
    rescode=int(str(r.status_code).strip())
    res = json.loads(answer) 
    
    url2 = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields2 + '&strictMatch=' + strictMatch;
    r2 = requests.get(url2, headers = {'app_id': app_id, 'app_key': app_key})
    answer2=r2.text
    rescode2=int(str(r2.status_code).strip())
    res2=json.loads(answer2)
    sumrescode=(rescode+rescode2)
    
    
    
    if sumrescode==400:
        res2=json.loads(answer2)
        
        try:
            e = time.time()
            resp=res["results"][0]["lexicalEntries"][0]['entries'][0]['senses'][0]['definitions'][0]
            WordC=res["results"][0]["lexicalEntries"][0]['lexicalCategory']['text']
            pron=res2["results"][0]["lexicalEntries"][0]['entries'][0]['pronunciations'][0]['phoneticSpelling']
            randWord = res["results"][0]["word"]
            
            wM=[randWord,resp,WordC,pron]
            
            query = "insert into word (word, Meaning, WordCat, wordPro, def_res, pro_res) values ('{}','{}','{}','{}','{}','{}')".format(randWord, resp, WordC, pron, json.dumps(res),pron)
            
            
            out = mysqlcon(query)

            d = time.time()
            print(c-d)
            print(d-e)
            

            return wM
        except:
            return getWord()
    else:
        q = "delete from wlist where word='{}'".format(word_id)
        mysqlcon(q)
        return getWord()






def genTenWords(user = None):

    if not user:
            ws = "SELECT word FROM wlist AS t1 JOIN (SELECT wlid FROM wlist where level={} ORDER BY RAND() LIMIT 10) as t2 ON t1.wlid=t2.wlid".format(6)
    else:
        qli = "select u.userid, c.lvl from users u, customers c where c.userid=u.userid and u.username ='{}'".format(user)
        ql = mysqlcon(qli)
        level = ql[0][1]
        ws = "SELECT word FROM wlist AS t1 JOIN (SELECT wlid FROM wlist where level={} ORDER BY RAND() LIMIT 10) as t2 ON t1.wlid=t2.wlid".format(level)
    z=0
    ws =mysqlcon(ws)
    print(ws)
    for w in words:
        print(ws[z][0])
        new=getWord(ws[z][0])
        print(new)
        words[w]=new
        z+=1
        print(words)
        
    
    print('done')
    return words


#=========================================== Before webapp function calls =====================================

genTenWords()



for w in words:
    print(words[w], 'g vhjkgvbbuibytvi')   
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
@app.route("/home")
@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for('index'))
    user = None
    return render_template("index.html",W1 = Ws[0], W2 = Ws[1], W3 = Ws[2], W4 = Ws[3], W5 = Ws[4], W6 = Ws[5], W7 = Ws[6], W8 = Ws[7], W9 = Ws[8], W10 = Ws[9], M1 = Ms[0], M2 = Ms[1], M3 = Ms[2], M4 = Ms[3], M5 = Ms[4], M6 = Ms[5], M7 = Ms[6], M8 = Ms[7], M9 = Ms[8], M10 = Ms[9],WC1 = WC[0], WC2 = WC[1], WC3 = WC[2], WC4 = WC[3], WC5 = WC[4], WC6 = WC[5], WC7 = WC[6], WC8 = WC[7], WC9 = WC[8], WC10 = WC[9], P1  = P[0], P2  = P[1], P3  = P[2], P4  = P[3], P5  = P[4], P6  = P[5], P7  = P[6], P8  = P[7], P9  = P[8], P10  = P[9], user=user)
    

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

    if rescode == 200:
        return render_template("lur.html", response = res["results"][0]["lexicalEntries"][0]['entries'][0]['senses'][0]['definitions'],res=res)
    else:
        return render_template("message.html", message="Word Not Found!")



@app.route('/signup')
def signup():
    return render_template('signup.html')
    

@app.route('/signupr', methods=['POST', 'GET'])
def signupr():
    name = request.form['fname']
    lname = request.form['lname']
    username = request.form['username']
    email = request.form['email']
    passwrd = request.form['password']
    level= request.form['level']
    level=int(level)
    try:
        signupdb(name, lname, username, email, passwrd, level)
        c=lncheck(email,passwrd)

        if c:
            user = c[1]           
            session["user"] = user

        return redirect(url_for('index'))
    except:
        return "Username or email already exists"


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/loginr', methods=['POST','GET'])
def loginr():
    email = request.form['email']
    password = request.form['password']
    c=lncheck(email,password)

    if c:
        user = c[1]
        
        session["user"] = user
        

        return redirect(url_for('index'))
    # try:
    else:
        return 'n'


@app.route('/knowit', methods=['GET', 'POST'])
def knowit():
    if "user" not in session:
        return redirect(url_for('login')) 
    user = session["user"]
    famword = request.form['word1']
    famword = famword.strip()
    print(famword)
    wid = mysqlcon("select wordid from word where word='{}'".format(famword))
    print(wid)
    kq = "insert into knows (cusid, wordid) value ((select cusid from customers c, users u where username = '{}' and u.userid = c.userid),{})".format(user, wid[0][0])
    fam = mysqlcon(kq)
    

    ws = "SELECT word FROM wlist AS t1 JOIN (SELECT wlid FROM wlist where level={} ORDER BY RAND() LIMIT 1) as t2 ON t1.wlid=t2.wlid".format(3)
    z=0
    ws =mysqlcon(ws)
    qren = "select w.word, w.Meaning, w.WordCat, w.wordPro from word w inner join (select r.wordid from rendered r natural left join knows k where k.wordid is NULL and r.cusid=(select cusid from customers c, users u where username = '{}' and u.userid = c.userid) order by rtime desc limit 9) as w2 on w.wordid = w2.wordid".format(user)
    wordM = mysqlcon(qren)
    print(wordM)
    print(ws)
    z=0
    for w in words:
        if w == 'word10':
            new = getWord(ws[0][0])
            words[w]= new
            print(words[w][0][0])
            wid = mysqlcon("select wordid from word where word='{}'".format(words[w][0]))
            kq = "insert into rendered (cusid, wordid) value ((select cusid from customers c, users u where username = '{}' and u.userid = c.userid),{})".format(user, wid[0][0])
            fam = mysqlcon(kq)
        else:
            word = wordM[z][0]
            resp = wordM[z][1]
            wc = wordM[z][2]
            prn = wordM[z][3]
            wM=[word,resp,wc,prn]
            new = wM
            words[w]= new

            print(wordM[z][0])
            z+=1

    n= 0 
    for w in words:
        Ws[n]=words[w][0]
        Ms[n]=words[w][1]
        WC[n]=words[w][2]
        P[n]=words[w][3]
        
        n+=1

            

    if "user" in session:
        user = session["user"]
        print(user)
        return render_template("index.html",W1 = Ws[0], W2 = Ws[1], W3 = Ws[2], W4 = Ws[3], W5 = Ws[4], W6 = Ws[5], W7 = Ws[6], W8 = Ws[7], W9 = Ws[8], W10 = Ws[9], M1 = Ms[0], M2 = Ms[1], M3 = Ms[2], M4 = Ms[3], M5 = Ms[4], M6 = Ms[5], M7 = Ms[6], M8 = Ms[7], M9 = Ms[8], M10 = Ms[9],WC1 = WC[0], WC2 = WC[1], WC3 = WC[2], WC4 = WC[3], WC5 = WC[4], WC6 = WC[5], WC7 = WC[6], WC8 = WC[7], WC9 = WC[8], WC10 = WC[9], P1  = P[0], P2  = P[1], P3  = P[2], P4  = P[3], P5  = P[4], P6  = P[5], P7  = P[6], P8  = P[7], P9  = P[8], P10  = P[9], user = user)
    
    


@app.route('/index')
def index():

    if "user" not in session:
        return redirect(url_for('home'))

    
    user = session["user"]
    genTenWords(user)
     
    n=0
    for w in words:
        wid = mysqlcon("select wordid from word where word='{}'".format(words[w][0]))
        print(wid)
        kq = "insert into rendered (cusid, wordid) value ((select cusid from customers c, users u where username = '{}' and u.userid = c.userid),{})".format(user, wid[0][0])
        fam = mysqlcon(kq)
    
        Ws[n]=words[w][0]
        Ms[n]=words[w][1]
        WC[n]=words[w][2]
        P[n]=words[w][3]
        
        n+=1
        


    if "user" in session:
        user = session["user"]
        print(user)
        return render_template("index.html",W1 = Ws[0], W2 = Ws[1], W3 = Ws[2], W4 = Ws[3], W5 = Ws[4], W6 = Ws[5], W7 = Ws[6], W8 = Ws[7], W9 = Ws[8], W10 = Ws[9], M1 = Ms[0], M2 = Ms[1], M3 = Ms[2], M4 = Ms[3], M5 = Ms[4], M6 = Ms[5], M7 = Ms[6], M8 = Ms[7], M9 = Ms[8], M10 = Ms[9],WC1 = WC[0], WC2 = WC[1], WC3 = WC[2], WC4 = WC[3], WC5 = WC[4], WC6 = WC[5], WC7 = WC[6], WC8 = WC[7], WC9 = WC[8], WC10 = WC[9], P1  = P[0], P2  = P[1], P3  = P[2], P4  = P[3], P5  = P[4], P6  = P[5], P7  = P[6], P8  = P[7], P9  = P[8], P10  = P[9], user = user)
    else:
        user = "Log In"
        print(user)
        return render_template("index.html",W1 = Ws[0], W2 = Ws[1], W3 = Ws[2], W4 = Ws[3], W5 = Ws[4], W6 = Ws[5], W7 = Ws[6], W8 = Ws[7], W9 = Ws[8], W10 = Ws[9], M1 = Ms[0], M2 = Ms[1], M3 = Ms[2], M4 = Ms[3], M5 = Ms[4], M6 = Ms[5], M7 = Ms[6], M8 = Ms[7], M9 = Ms[8], M10 = Ms[9],WC1 = WC[0], WC2 = WC[1], WC3 = WC[2], WC4 = WC[3], WC5 = WC[4], WC6 = WC[5], WC7 = WC[6], WC8 = WC[7], WC9 = WC[8], WC10 = WC[9], P1  = P[0], P2  = P[1], P3  = P[2], P4  = P[3], P5  = P[4], P6  = P[5], P7  = P[6], P8  = P[7], P9  = P[8], P10  = P[9], user = user)
    

@app.route('/lo')
def logout():
    p=session.pop('user')
    return redirect(url_for('home'))
    


if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)












#================================================Test Commands====================================================
schedule.every().day.at("10:30").do(genTenWords)

while True:
    schedule.run_pending()
    time.sleep(1)