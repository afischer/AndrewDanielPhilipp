from flask import Flask,render_template,request,redirect,url_for
from time import strftime, gmtime
import sqlite3,csv

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",
                           projectName="Our Project"
                          )

# base.html contains the header, footer, and linnks to the stylesheets/js
# Should only go here for testing purposes.
@app.route("/base")
def base():
    return render_template("base.html",
                           projectName="Our Project"
                          )

@app.route("/poststemplate")
def postsTemplate():
    return render_template("postsTemplate.html")


if __name__=="__main__":
    app.debug=True
    app.run()
