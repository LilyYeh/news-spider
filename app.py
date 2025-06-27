from flask import Flask, jsonify, render_template
from const import urls, medias, categories
from news import top, hot, society, political, international, lifestyle, keyword
from concurrent.futures import ThreadPoolExecutor
import gc
import sys

#top.chinatimes()
#sys.exit()

app = Flask(__name__)

@app.route("/")
def index():
    with ThreadPoolExecutor() as executor:
        # 提交任務給執行緒池
        futures = {
            'top_udn': executor.submit(top.udn),
            'top_itn': executor.submit(top.itn),
            'top_apple': executor.submit(top.apple),
            'top_setn': executor.submit(top.setn),
            'top_ettoday': executor.submit(top.ettoday),
            #'top_chinatimes': executor.submit(top.chinatimes),
            'hot_yahoo': executor.submit(hot.yahoo_more),
            'hot_udn': executor.submit(hot.udn),
            'hot_itn': executor.submit(hot.itn),
            'hot_apple': executor.submit(hot.apple),
            'hot_setn': executor.submit(hot.setn),
            'hot_tvbs': executor.submit(hot.tvbs),
            'hot_ettoday': executor.submit(hot.ettoday),
            'hot_chinatimes': executor.submit(hot.chinatimes),
            'society_udn': executor.submit(society.udn),
            'society_itn': executor.submit(society.itn),
            'society_apple': executor.submit(society.apple),
            'society_setn': executor.submit(society.setn),
            'society_chinatimes': executor.submit(society.chinatimes),
            'society_ettoday': executor.submit(society.ettoday),
            'political_udn': executor.submit(political.udn),
            'political_itn': executor.submit(political.itn),
            'political_apple': executor.submit(political.apple),
            'political_setn': executor.submit(political.setn),
            'political_chinatimes': executor.submit(political.chinatimes),
            'political_ettoday': executor.submit(political.ettoday),
            'international_udn': executor.submit(international.udn),
            'international_itn': executor.submit(international.itn),
            'international_apple': executor.submit(international.apple),
            'international_setn': executor.submit(international.setn),
            'international_chinatimes': executor.submit(international.chinatimes),
            'international_ettoday': executor.submit(international.ettoday),
            'lifestyle_udn': executor.submit(lifestyle.udn),
            'lifestyle_itn': executor.submit(lifestyle.itn),
            'lifestyle_apple': executor.submit(lifestyle.apple),
            'lifestyle_setn': executor.submit(lifestyle.setn),
            'lifestyle_chinatimes': executor.submit(lifestyle.chinatimes),
            'lifestyle_ettoday': executor.submit(lifestyle.ettoday),
            'keyword_udn': executor.submit(keyword.udn),
            'keyword_itn': executor.submit(keyword.itn),
            'keyword_setn': executor.submit(keyword.setn),
            'keyword_tvbs': executor.submit(keyword.tvbs),
            'keyword_chinatimes': executor.submit(keyword.chinatimes),
        }

        news = {
            "top": {
                "udn": futures['top_udn'].result(),
                "itn": futures['top_itn'].result(),
                "apple": futures['top_apple'].result(),
                "setn": futures['top_setn'].result(),
                #"chinatimes": futures['top_chinatimes'].result(),
                "ettoday": futures['top_ettoday'].result(),
            },
            "hot": {
                "yahoo": futures['hot_yahoo'].result(),
                "udn": futures['hot_udn'].result(),
                "itn": futures['hot_itn'].result(),
                "apple": futures['hot_apple'].result(),
                "setn": futures['hot_setn'].result(),
                "tvbs": futures['hot_tvbs'].result(),
                "chinatimes": futures['hot_chinatimes'].result(),
                "ettoday": futures['hot_ettoday'].result(),
            },
            "society": {
                "udn": futures["society_udn"].result(),
                "itn": futures["society_itn"].result(),
                "apple": futures["society_apple"].result(),
                "setn": futures["society_setn"].result(),
                "chinatimes": futures["society_chinatimes"].result(),
                "ettoday": futures["society_ettoday"].result(),
            },
            "political": {
                "udn": futures["political_udn"].result(),
                "itn": futures["political_itn"].result(),
                "apple": futures["political_apple"].result(),
                "setn": futures["political_setn"].result(),
                "chinatimes": futures["political_chinatimes"].result(),
                "ettoday": futures["political_ettoday"].result(),
            },
            "international": {
                "udn": futures["international_udn"].result(),
                "itn": futures["international_itn"].result(),
                "apple": futures["international_apple"].result(),
                "setn": futures["international_setn"].result(),
                "chinatimes": futures["international_chinatimes"].result(),
                "ettoday": futures["international_ettoday"].result(),
            },
            "lifestyle": {
                "udn": futures["lifestyle_udn"].result(),
                "itn": futures["lifestyle_itn"].result(),
                "apple": futures["lifestyle_apple"].result(),
                "setn": futures["lifestyle_setn"].result(),
                "chinatimes": futures["lifestyle_chinatimes"].result(),
                "ettoday": futures["lifestyle_ettoday"].result(),
            },
            "keyword": {
                "udn": futures["keyword_udn"].result(),
                "itn": futures["keyword_itn"].result(),
                "setn": futures["keyword_setn"].result(),
                "tvbs": futures["keyword_tvbs"].result(),
                "chinatimes": futures["keyword_chinatimes"].result(),
            }
        }

    rendered = render_template(
        "index.html",
        urls=urls,
        news=news,
        medias=medias.medias,
        categories=categories.categories
    )

    # 主動釋放記憶體
    del futures
    del news
    gc.collect()

    return rendered


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
