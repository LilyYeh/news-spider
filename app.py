from flask import Flask, jsonify, render_template
from const import urls, medias, categories
from news import hot, society, political, international, lifestyle
import sys

app = Flask(__name__)
@app.route("/")
def index():
    news = {
        "hot": {
            "udn": hot.udn(),
            "itn": hot.itn(),
            "apple": hot.apple(),
            "setn": hot.setn()
        },
        "society": {
            "udn": society.udn(),
            "itn": society.itn(),
            "apple": society.apple(),
            "setn": society.setn()
        },
        "political": {
            "udn": political.udn(),
            "itn": political.itn(),
            "apple": political.apple(),
            "setn": political.setn(),
        },
        "international": {
            "udn": international.udn(),
            "itn": international.itn(),
            "apple": international.apple(),
            "setn": international.setn(),
        },
        "lifestyle": {
            "udn": lifestyle.udn(),
            "itn": lifestyle.itn(),
            "apple": None,
            "setn": lifestyle.setn(),
        }

    }

    return render_template(
        "index.html",
        urls=urls,
        news=news,
        medias=medias.medias,
        categories=categories.categories
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)