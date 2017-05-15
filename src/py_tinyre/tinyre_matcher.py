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

class TinyREMatcher():
    def __init__(self, matchers):
        self.__matchers = matchers
        self.__i = 0

    def accept(self, c):
        cur_matcher = self.__matchers[self.__i]
        state = cur_matcher.accept(c)
        while state == SKIP_MATCHER:
            self.__i += 1
            if self.__i == len(self.__matchers):
                return SUCCESS
            cur_matcher = self.__matchers[self.__i]
            state = cur_matcher.accept(c)

        if state == FAIL:
            return FAIL
        if state == NEXT_MATCHER_AND_CHAR:
            self.__i += 1
            if self.__i == len(self.__matchers):
                return SUCCESS

        return NEXT_CHAR
