import load
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def i():
  return render_template("index.html")

@app.route("/post",methods=["POST","GET"])
def p():
  tts = load.TextToSpeech()
  pr = request.form
  return render_template("s.html",mp3=tts.get_pronunciation(pr['t']))
app.run(host="0.0.0.0",port=8080)