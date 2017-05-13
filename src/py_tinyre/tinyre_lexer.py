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

class TinyRELexer():
    def __init__(self, pattern):
        self.__pattern = pattern
        self.__tokens = []

    def tokens(self):
        self.__prepare()
        while self.__i<len(self.__pattern):
            c = self.__pattern[self.__i]
            self.__handle_char(c)
            self.__i += 1

        self.__check_state()
        return self.__tokens

    def __prepare(self):
        self.__i = 0
        self.__state = START
        self.__cur_collection = ""

    def __handle_char(self, c):
        if self.__state == START:
            self.__handle_start(c)
        elif self.__state == AFTER_CHAR:
            self.__handle_after_char(c)
        elif self.__state == GOBBLE_CHAR:
            self.__handle_gobble_char(c)

    def __check_state(self):
        if self.__state != START:
            raise Exception()

    def __handle_start(self, c):
        if c == '.':
            self.__tokens.append((ANY_CHAR, '\0'))
            self.__state = AFTER_CHAR
        elif c == '[':
            self.__state = GOBBLE_CHAR
        else:
            raise Exception()

    def __handle_after_char(self, c):
        if c == '?' or c == '+' or c == '*':
            self.__tokens.append((GLOB, c))
        else:
            self.__i -= 1 # unget
        self.__state = START

    def __handle_gobble_char(self, c):
        if c == ']':
            self.__tokens.append((CHAR_COLLECTION, self.__cur_collection))
            self.__cur_collection = ""
            self.__state = AFTER_CHAR
        else:
            self.__cur_collection += c
