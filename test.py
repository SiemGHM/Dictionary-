
Wt1 = "<button name="subject" type="submit" value='{}'>Know It</button>".format(Ws[0]), Wt2 = "{}".format(Ws[1]), Wt3 = "{}".format(Ws[2]), Wt4 = "{}".format(Ws[3]), Wt5 ="{}".format(Ws[4]), Wt6 = "{}".format(Ws[5]), Wt7 = "{}".format(Ws[6]), Wt8 = "{}".format(Ws[7]), Wt9 = "{}".format(Ws[8]), Wt10 = "{}".format(Ws[9])
<button name="subject" type="submit" value='{}'>Know It</button>
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
            print('"{}",'.format(i), end = "", file=p)
