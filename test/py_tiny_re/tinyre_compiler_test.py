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
from py_tinyre.tinyre_compiler import TinyRECompiler
from py_tinyre.node_matcher import *
from py_tinyre.tinyre_parser import TinyREParser
from py_tinyre.tinyre_lexer import TinyRELexer

class TestTinyRECompiler(unittest.TestCase):
    def test(self):
        nodes = [(ZERO_OR_MORE, (CHAR_COLLECTION, "a-z")), (ONE_OR_MORE, (ANY_CHAR, "\0"))]
        matchers = TinyRECompiler().compile(nodes)
        self.assertEquals(2, len(matchers))
        self.assertEquals(ZeroOrMoreMatcher, type(matchers[0]))
        self.assertEquals(OneOrMoreMatcher, type(matchers[1]))

    def test2(self):
        l = TinyRELexer()
        p = TinyREParser()
        c = TinyRECompiler()
        re = c.compile(p.parse(l.tokenize("[p][a][t][t][e][r][n]")))
        self.assertEquals(7, len(re))
        for i in range(7):
            self.assertEquals(OneMatcher, type(re[i]))


if __name__ == '__main__':
    unittest.main()
