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
from py_tinyre.char_collection_lexer import CharCollectionLexer

class CharCollectionMatcher():
    def __init__(self, tokens):
        assert type(tokens) == list
        self.__tokens = tokens

    def __str__(self):
        return "CharCollectionMatcher({0})".format(self.__tokens)

    def match(self, c):
        self.__i = 0
        if self.__tokens[self.__i][OP_CODE] == NEG:
            self.__i += 1
            return not self.__match(c)
        else:
            return self.__match(c)

    def __match(self, c):
        while self.__i < len(self.__tokens):
            if self.__match_token(c):
                return True
            self.__i += 1

        return False

    def __match_token(self, c):
        token = self.__tokens[self.__i]
        if token[OP_CODE] == CHAR_RANGE:
            return self.__match_range(token[VALUE], c)
        elif token[OP_CODE] == ONE_CHAR:
            return c == token[VALUE]
        else:
            raise Exception()

    def __match_range(self, ft, c):
        f, t = ft
        return c >= f and c <= t
