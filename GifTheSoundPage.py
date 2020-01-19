import json
import random

from dotenv import load_dotenv
from flask import Flask, render_template, request, send_from_directory

from GifGenerator import GifGenerator
from words.SimpleWords import SimpleWords, WordType

load_dotenv()

app = Flask(__name__)
words_by_type = SimpleWords().search_words()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/favicon.png')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.png', mimetype='image/png')


@app.route('/load_gifs', methods=['POST'])
def load_gifs():
    options = request.get_json()
    search_text = options["searchText"]
    do_fast_search = options["doFastSearch"]
    use_any_words = options["anyWords"]

    word_types = []
    if not use_any_words:
        word_types_options = options["wordTypes"]
        if word_types_options["nouns"]:
            word_types.append(WordType.NOUNS)
        if word_types_options["verbs"]:
            word_types.append(WordType.VERBS)
        if word_types_options["adverbs"]:
            word_types.append(WordType.ADVERBS)
        if word_types_options["adjectives"]:
            word_types.append(WordType.ADJECTIVES)

    # returns list of gifs by word.. "ape": [gif1, gif2, gif3], "flower": [gif5]..
    gif_generator = GifGenerator.create(do_fast_search)
    gifs_by_words = gif_generator.search_gifs_for_text(search_text, word_types)
    all_urls = []
    for wordgif_dict in gifs_by_words:
        for word, gifs in wordgif_dict.items():
            random_gif = random.choice(gifs)
            all_urls.append({"word": word, "url": random_gif.images.downsized.url})
    return json.dumps(all_urls)


if __name__ == "__main__":
    app.run()
