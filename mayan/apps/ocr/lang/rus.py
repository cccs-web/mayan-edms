# -*- coding: utf-8 -*-
from __future__ import absolute_import

import re

from . import BackendBase


class LanguageBackend(BackendBase):
    def check_word(self, word):
        ALL_ALPHANUM = re.compile('([0-9ёйцукенгшщзхъфывапролджэячсмитьбю])', re.I)
        NON_ALPHANUM = re.compile('([^0-9ёйцукенгшщзхъфывапролджэячсмитьбю])', re.I)

        TOO_MANY_VOWELS = re.compile('[ёуеыаоэяию]{3}', re.I)
        TOO_MANY_CONSONANTS = re.compile('[йцкнгшщзхъфвпрлджчсмтьб{5}', re.I)
        ALL_ALPHA = re.compile('^[ёйцукенгшщзхъфывапролджэячсмитьбю]+$', re.I)
        SINGLE_LETTER_WORDS = re.compile('^[уквояси]$', re.I)

        # (L) If a string is longer than 25 characters, it is garbage
        if len(word) > 25:
            return None

        # (A) If a string's ratio of alphanumeric characters to total
        # characters is less than 50%, the string is garbage
        if len(ALL_ALPHANUM.findall(word)) < len(word) / 2:
            return None

        # Remove word if all the letters in the word are non alphanumeric
        if len(NON_ALPHANUM.findall(word)) == len(word):
            return None

        # Removed words with too many consecutie vowels
        if TOO_MANY_VOWELS.findall(word):
            return None

        # Removed words with too many consecutie consonants
        if TOO_MANY_CONSONANTS.findall(word):
            return None

        # Only allow specific single letter words
        if len(word) == 1 and not SINGLE_LETTER_WORDS.findall(word):
            return None

        return word
