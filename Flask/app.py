from flask import Flask
from flask import render_template
from flask import request
import subprocess

app = Flask("realmyapp")
@app.route("/form")
def myform():
    data = render_template("myform.html")
    return data
@app.route("/tech", methods=["GET"])
def mycmd():
    mycmd = request.args.get("cmd")
    return "<pre>" + subprocess.getoutput(mycmd) + "</pre>"

