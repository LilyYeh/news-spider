from flask import Flask, jsonify, render_template
from const import urls, medias, categories
from news import top, hot, society, political, international, lifestyle, series
import sys

app = Flask(__name__)
@app.route("/")
def index():
    news = {
        "top": {
            "udn": top.udn(),
            "itn": top.itn(),
            "apple": top.apple(),
            "setn": top.setn(),
        },
        "hot": {
            "yahoo": hot.yahoo(),
            "udn": hot.udn(),
            "itn": hot.itn(),
            "apple": hot.apple(),
            "setn": hot.setn(),
            "tvbs": hot.tvbs(),
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
            "apple": lifestyle.apple(),
            "setn": lifestyle.setn(),
        },
        "series": {
            "udn": series.udn(),
            "setn": series.setn(),
            "tvbs": series.tvbs(),
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