import os

from nltk.corpus import wordnet

WORDS_PATH = os.path.dirname(__file__)
NOUNS_PATH = os.path.join(WORDS_PATH, "noun.txt")
ADJS_PATH = os.path.join(WORDS_PATH, "adj.txt")
ADVS_PATH = os.path.join(WORDS_PATH, "adv.txt")
VERBS_PATH = os.path.join(WORDS_PATH, "verb.txt")


class SimpleWords:
    words_by_type = {}

    def search_words(self):
        for file in os.listdir(WORDS_PATH):
            if file.endswith(".txt"):
                filename = os.path.splitext(os.path.basename(file))[0]
                self.words_by_type[filename] = self.search_words_in_file(os.path.join(WORDS_PATH, file))

        return self.words_by_type

    def search_words_in_file(self, filename):
        with open(filename, 'r') as file:
            words = file.readlines()
        return [word.replace('\n', '') for word in words]

    def nouns(self):
        return self.search_words_in_file(NOUNS_PATH)

    def adverbs(self):
        return self.search_words_in_file(ADVS_PATH)

    def adjects(self):
        return self.search_words_in_file(ADJS_PATH)

    def verbs(self):
        return self.search_words_in_file(VERBS_PATH)

    def nouns_in_text(self, text: str):
        text = text.split(" ")
        clean_text = []
        for word in text:
            clean_text.append(''.join(e for e in word if e.isalnum()))
        nouns = self.nouns()
        res = []
        for word in clean_text:
            if word in nouns:
                res.append(word)
            else:
                word_morphed = wordnet.morphy(word)
                if word_morphed in nouns:
                    res.append(word_morphed)
        return res
