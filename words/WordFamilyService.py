from nltk.corpus import wordnet as wn
from words.WordFamily import WordFamily

class WordFamilyService:
    wordnet_families = {
        "noun": wn.NOUN,
        "adj": wn.ADJ,
        "verb": wn.VERB,
        "adv": wn.ADV
    }

    @classmethod
    def get(cls, family_type: str):
        if not family_type in cls.wordnet_families:
            raise ValueError(f"{family_type} is not in dictionary!")
        wn_family_type = cls.wordnet_families.get(family_type)
        words = list(wn.all_synsets(wn_family_type))
        return WordFamily(words=words, family_type=family_type)

    @classmethod
    def get_all(cls):
        word_families = []
        for family_type in cls.wordnet_families:
            word_families.append(cls.get(family_type))
        return word_families

