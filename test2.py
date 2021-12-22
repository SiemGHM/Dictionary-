from flask import Flask,render_template, request, request, url_for, session, jsonify, make_response, redirect 



app=Flask(__name__)



@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")




if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)