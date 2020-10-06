from flask import Flask,render_template, request, request, url_for, session


app=Flask(__name__)
app.secret_key="heythere"



@app.route("/")
def home():
    return render_template("index.html")
    





if __name__=='__main__':
    app.run(debug=True)
