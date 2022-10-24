import load
from flask import Flask, render_template, request
from markupsafe import escape
app = Flask(__name__)
n = None
y = "New update coming soon."
v = "2.2"
patch = n
@app.route("/")
def i():
  if patch is None:
    return render_template("index.html",v=v)
  else:
    return patch

@app.route("/post",methods=["POST","GET"])
def p():
  if patch is None:
    tts = load.TextToSpeech()
    pr = request.form
    return render_template("s.html",mp3=tts.get_pronunciation(pr['t']),t=pr['t'],escape=escape)
app.run(host="0.0.0.0",port=8080)