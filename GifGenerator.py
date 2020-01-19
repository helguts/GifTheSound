import os
import random

import giphy_client
from giphy_client.rest import ApiException

from words.SimpleWords import SimpleWords


class GifGenerator:
    __api_key = ""
    __api_instance = giphy_client.DefaultApi()

    amount = 25
    offset = 0  # int | An optional results offset. Defaults to 0. (optional) (default to 0)
    rating = 'g'  # str | Filters results by specified rating. (optional)
    lang = 'en'  # str | Specify  default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
    fmt = 'json'  # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

    @classmethod
    def create(cls, with_fast_search: bool = False):
        generator = GifGenerator()
        if with_fast_search:
            generator.amount = 1
            generator.offset = random.randrange(25)
        return generator

    def __init__(self):
        self.__api_key = os.getenv("GIPHY_API_KEY")

    def search(self, search_term):
        try:
            # Search Endpoint
            api_response = self.__api_instance.gifs_search_get(self.__api_key, search_term, limit=self.amount,
                                                               offset=self.offset, rating=self.rating,
                                                               lang=self.lang, fmt=self.fmt)

            # all 25 gifs..
            return api_response.data if api_response else None
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

    def search_gifs_for_text(self, text):
        nouns_in_text = SimpleWords().nouns_in_text(text)

        gifs_by_word = []
        for noun in nouns_in_text:
            if not noun:
                continue
            gifs = self.search(noun)
            if gifs:
                gifs_by_word.append({noun: gifs})
        return gifs_by_word
