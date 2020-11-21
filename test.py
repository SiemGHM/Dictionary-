


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
