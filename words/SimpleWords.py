import os
from enum import Enum

from nltk.corpus import wordnet

WORDS_PATH = os.path.dirname(__file__)
NOUNS_PATH = os.path.join(WORDS_PATH, "noun.txt")
ADJS_PATH = os.path.join(WORDS_PATH, "adj.txt")
ADVS_PATH = os.path.join(WORDS_PATH, "adv.txt")
VERBS_PATH = os.path.join(WORDS_PATH, "verb.txt")


class WordType(Enum):
    NOUNS = 1
    VERBS = 2
    ADJECTIVES = 3
    ADVERBS = 4


class SimpleWords:
    words_by_type = {}

    def search_words(self):
        for file in os.listdir(WORDS_PATH):
            if file.endswith(".txt"):
                self.search_words_in_file(os.path.join(WORDS_PATH, file))

        return self.words_by_type

    def search_words_in_file(self, filename):
        if filename in self.words_by_type:
            return self.words_by_type.get(filename)

        with open(filename, 'r') as file:
            words = file.readlines()
        words = [word.replace('\n', '').lower() for word in words]
        self.words_by_type[filename] = words
        return words

    def nouns(self):
        return [noun for noun in self.search_words_in_file(NOUNS_PATH) if len(noun) > 1]

    def adverbs(self):
        return self.search_words_in_file(ADVS_PATH)

    def adjects(self):
        return self.search_words_in_file(ADJS_PATH)

    def verbs(self):
        return self.search_words_in_file(VERBS_PATH)

    def get_words_by_type(self, word_type: WordType):
        if WordType.NOUNS == word_type:
            return self.nouns()
        elif WordType.VERBS == word_type:
            return self.verbs()
        elif WordType.ADJECTIVES == word_type:
            return self.adjects()
        elif WordType.ADVERBS == word_type:
            return self.adverbs()

    def words_in_text(self, text: str, word_types):
        clean_text = self.do_cleanup_text(text)
        words_of_types = [self.get_words_by_type(word_type) for word_type in word_types]
        res = []
        for word in clean_text:
            for words_of_type in words_of_types:
                if word in words_of_type:
                    res.append(word)
                    break
                else:
                    word_morphed = wordnet.morphy(word)
                    if word_morphed in words_of_type:
                        res.append(word_morphed)
                        break
        return res

    def do_cleanup_text(self, text):
        text = text.replace("\n", " ").split(" ")
        clean_text = []
        for word in text:
            cleaned_word = ''.join(e for e in word if e.isalnum())
            clean_text.append(cleaned_word.lower())
        return clean_text
