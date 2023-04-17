from flask import Flask, request, render_template
import codecs
app = Flask(__name__)

@app.route("/")
def bbs():

    file = codecs.open("articles.txt", "r", "utf-8")
    lines = file.readlines()
    file.close()

    return render_template("bbs.html", lines = lines)

@app.route("/result", methods=["POST"])
def result():
    article = request.form["article"]
    name = request.form["name"]

    file = codecs.open("articles.txt", "a", "utf-8")
    file.write(article + "," + name + "\n")
    file.close()

    return render_template("bbs_result.html", article = article, name = name)