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
import unittest
import env
from py_tinyre.constants import *
from py_tinyre.tinyre_lexer import TinyRELexer

class TestTinyRELexer(unittest.TestCase):
    def test(self):
        self.assertEqual([
            (CHAR_COLLECTION, "a-z"),
            (GLOB, "*"),
            (ANY_CHAR, "\0"),
            (GLOB, "+")
        ], TinyRELexer().tokenize("[a-z]*.+"))

    def testPattern(self):
        self.assertEqual([
            (CHAR_COLLECTION, "p"),
            (CHAR_COLLECTION, "a"),
            (CHAR_COLLECTION, "t"),
            (CHAR_COLLECTION, "t"),
            (CHAR_COLLECTION, "e"),
            (CHAR_COLLECTION, "r"),
            (CHAR_COLLECTION, "n"),
        ], TinyRELexer().tokenize("[p][a][t][t][e][r][n]"))


if __name__ == '__main__':
    unittest.main()
