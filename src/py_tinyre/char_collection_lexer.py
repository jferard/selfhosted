"""Self Hosted - A Self Hosted compiler project
      Copyright (C) 2017 J. Férard <https://github.com/jferard>

   This file is part of Self Hosted.

   Self Hosted is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   Self Hosted is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>."""
from py_tinyre.constants import *

class CharCollectionLexer():
    def tokenize(self, char_collection):
        return _CharCollectionLexerFor(char_collection).tokens()

class _CharCollectionLexerFor():
    """Take chars and build [not] [interval] [single]"""
    def __init__(self, char_collection):
        if len(char_collection) == 0:
            raise Exception()
        self.__char_collection = char_collection

    def tokens(self):
        if len(self.__char_collection) == 1:
            self.__tokens = [(ONE_CHAR, self.__char_collection[0])]
        else:
            self.__get_tokens_from_some_ranges()
        return self.__tokens

    def __get_tokens_from_some_ranges(self):
        self.__i = 0
        self.__tokens = []
        self.__process_head_chars()
        self.__process_tail_chars()

    def __process_head_chars(self):
        if self.__char_collection[self.__i] == '^':
            self.__tokens.append((NEG, '\0'))
            self.__i += 1
        if self.__char_collection[self.__i] == '-':
            self.__tokens.append((ONE_CHAR, '-'))
            self.__i += 1

    def __process_tail_chars(self):
        while self.__i<len(self.__char_collection):
            c = self.__char_collection[self.__i]
            if not self.__process_range(c):
                self.__tokens.append((ONE_CHAR, c))
            self.__i += 1

    def __process_range(self, begin_c):
        if self.__i+2 < len(self.__char_collection) and self.__char_collection[self.__i+1] == '-':
            end_c = self.__char_collection[self.__i+2]
            self.__tokens.append((CHAR_RANGE, (begin_c, end_c)))
            self.__i += 2
            return True
        else:
            return False
