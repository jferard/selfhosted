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

class OneMatcher():
    def __init__(self, token_matcher):
        self.__token_matcher = token_matcher

    def accept(self, c):
        if self.__token_matcher.match(c):
            return NEXT_MATCHER_AND_CHAR
        else:
            return FAIL

class ZeroOrMoreMatcher():
    def __init__(self, token_matcher):
        self.__token_matcher = token_matcher

    def accept(self, c):
        if self.__token_matcher.match(c):
            return NEXT_CHAR
        else:
            return NEXT_MATCHER

class ZeroOrOneMatcher():
    def __init__(self, token_matcher):
        self.__token_matcher = token_matcher

    def accept(self, c):
        if self.__token_matcher.match(c):
            return NEXT_CHAR_AND_MATCHER
        else:
            return NEXT_MATCHER

class OneOrMoreMatcher():
    def __init__(self, token_matcher):
        self.__token_matcher = token_matcher
        self.__first = True

    def accept(self, c):
        if self.__first:
            self.__first = False
            if self.__token_matcher.match(c):
                return NEXT_CHAR
            else:
                return FAIL
        else:
            if self.__token_matcher.match(c):
                return NEXT_CHAR
            else:
                return NEXT_MATCHER
