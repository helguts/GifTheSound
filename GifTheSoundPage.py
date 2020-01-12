import json
import random

from dotenv import load_dotenv
from flask import Flask, render_template, request

from GifGenerator import GifGenerator
from words.SimpleWords import SimpleWords

load_dotenv()

app = Flask(__name__)
words_by_type = SimpleWords().search_words()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/load_gifs', methods=['POST'])
def load_gifs():
    search_text = request.form.get("search_text")

    # returns list of gifs by word.. "ape": [gif1, gif2, gif3], "flower": [gif5]..
    gifs_by_words = GifGenerator().search_gifs_for_text(search_text)
    all_urls = []
    for wordgif_dict in gifs_by_words:
        for word, gifs in wordgif_dict.items():
            random_gif = random.choice(gifs)
            all_urls.append({"word": word, "url": random_gif.images.downsized.url})
    return json.dumps(all_urls)


if __name__ == "__main__":
    app.run()
