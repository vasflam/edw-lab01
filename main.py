from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def show_products():
    data = {}
    try:
        with open("data.json", "r") as fp:
            data = json.load(fp)
    except:
        pass

    return render_template("index.html", data=data)
