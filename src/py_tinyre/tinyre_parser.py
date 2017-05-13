# -*- coding: utf-8 -*-
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

class TinyREParser():
    def __init__(self, tokens):
        self.__tokens = tokens

    def parse(self):
        self.__i = 0
        self.__l = []
        while self.__i+1<len(self.__tokens):
            token = self.__tokens[self.__i]
            next_token = self.__tokens[self.__i+1]

            self.__check_first_token(token)
            self.__try_parse_pair(token, next_token)
            self.__i += 1

        self.__try_parse_last()
        return self.__l

    def __check_first_token(self, token):
        if token[OP_CODE] == GLOB:
            raise Exception()

    def __try_parse_pair(self, token, next_token):
        if next_token[OP_CODE] == GLOB:
            self.__parse_glob(token, next_token)
        else:
            self.__l.append((ONE, token))

    def __parse_glob(self, token, next_token):
        if next_token[VALUE] == '+':
            self.__l.append((ONE_OR_MORE, token))
        elif next_token[VALUE] == '*':
            self.__l.append((ZERO_OR_MORE, token))
        elif next_token[VALUE] == '?':
            self.__l.append((ZERO_OR_ONE, token))
        self.__i += 1 # gobble glob

    def __try_parse_last(self):
        if self.__i<len(self.__tokens):
            token = tokens[self.__i]
            self.__check_first_token(token)
            self.__l.append((ONE, token))
