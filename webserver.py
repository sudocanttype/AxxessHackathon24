import flask
from flask import Flask, render_template
import os
app = Flask(__name__)
app = Flask(__name__,
            static_url_path='',
            static_folder='static')



@app.route("/upload")
def upload():
   print("hi")

   return "hi"

@app.route("/<name>",methods=['GET','POST'])
def index(name):
    if flask.request.method == "GET" :
       if "html" in name:
           return render_template(name)
       else:
           return flask.send_file('static/'+name)

    else:
       if name == "upload":
           uploaded_files = flask.request.files.getlist("file[]")
           print(uploaded_files)

       return ""


if __name__ == '__main__':
   app.run(debug = True)
