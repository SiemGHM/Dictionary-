


import pymysql
import json

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
# <script>
#   $( function() {
#     var availableTags = [
#       "ActionScript",
#       "AppleScript",
#       "Asp",
#       "BASIC",
#       "C",
#       "C++",
#       "Clojure",
#       "COBOL",
#       "ColdFusion",
#       "Erlang",
#       "Fortran",
#       "Groovy",
#       "Haskell",
#       "Java",
#       "JavaScript",
#       "Lisp",
#       "Perl",
#       "PHP",
#       "Python",
#       "Ruby",
#       "Scala",
#       "Scheme"
#     ];
#     $( "#tags" ).autocomplete({
#       source: availableTags
#     });
#   } );
#   </script>



with open('dict.txt', 'r') as f:
    with open('siem.txt','a') as p:
        for i in f:
            i = i.strip()
            if "'" not in i:
                q = 'Insert into wlist (word) value ("{}")'.format(i)
                try:
                    mysqlcon(q)
                except:
                    pass
                
