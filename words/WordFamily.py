import os


class WordFamily:
    __words = []
    type = ''

    def __init__(self, words, family_type):
        self.__words = words
        self.type = family_type

    def as_simple_name_list(self, ordered: bool = True):
        simple_names_list = [word._lemma_names[0].replace("_", " ") for word in self.__words]
        if ordered:
            simple_names_list.sort()
        return list(dict.fromkeys(simple_names_list))

    def to_file(self, ordered: bool = True):
        simple_name_list = self.as_simple_name_list(ordered)
        filename = os.path.join(os.path.dirname(__file__), f"{self.type}.txt")
        with open(filename, 'w') as file:
            file.write('\n'.join(str(word) for word in simple_name_list))
            file.close()
