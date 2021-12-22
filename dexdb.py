# import mysql.connector


# dbconfig = { 'host': '127.0.0.1',
# 'user': 'SiemGHM',
# 'password': '$iemGH12',
# 'database': 'dexdb', }

# conn= mysql.connector.connect(**dbconfig)


import pymysql
import json







def dictDB(word):
    query = "select word, Meaning, WordCat, wordPro, def_res, pro_res from word where word.word='{}'".format(word)
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




# word='yip'

# wordM = dictDB(word)

# if wordM:
#         word = wordM[0][0]
#         resp = wordM[0][1]
#         wc = wordM[0][2]
#         prn = wordM[0][3]
#         wM=[word,resp,wc,prn]
#         print(wM)

# defo = dictDB(word)
# print(defo)
# toex = defo[0][4]

# print(toex)
# toex = json.loads(toex)

# print(extracted)
# print(extracted['id'])

# print('RUNNNNNNNNNNNNNNNNNNNNNNNNNINNNNNNNNNNNNNNNNNNNNNNNNNNNNN')
# print(defo[0][1]['results'])

# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"+toex['id'])



# print(toex)


# query = "insert into users (username,email, passwd) values ('{}','{}','{}')".format('siemm', 'emalil', 'passrdd')
# ex = mysqlcon(query)
# uID = mysqlcon("select UserID from users where username='{}'".format('siemm'))
# print(uID[0][0])


# def lncheck(email,password):
#     print(email)
#     pw = mysqlcon("select passwd from users where email='{}'".format(email))
#     print(pw)
#     print(pw[0][0], password)
#     if password.strip() == pw[0][0]:
#         return True
#     else:
# #         return False

# h = lncheck('siemghirmai2@gmial.com','asdasd')
# print(h)

# famword = 'advertisement'
# wid = mysqlcon("select wordid from word where word='{}'".format(famword))
# print(wid[0][0])
# kq = "insert into knows (cusid, wordid) value ((select cusid from customers c, users u where username = '{}' and u.userid = c.userid),{})".format('Hadish', wid[0][0])
# fam = mysqlcon(kq)

with open("cuh.txt", "r") as f:
    words= f.readlines()
    for word in words:
        print(word.strip())
        
        kq = "update wlist set level=6 where word='{}'".format(word.strip())
        q= "insert into wlist (word, level) value('{}',6)".format(word.strip())

        try:
            fam= mysqlcon(q)
        except:
            fam = mysqlcon(kq)


