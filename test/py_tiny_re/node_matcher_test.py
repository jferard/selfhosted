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
from py_tinyre.node_matcher import *
from py_tinyre.char_collection_matcher import *

class TestNodeMatcher(unittest.TestCase):
    def testOne(self):
        m = OneMatcher(CharCollectionMatcher([(ONE_CHAR, "a")]))
        self.assertEquals(NEXT_MATCHER_AND_CHAR, m.accept('a'))

    def testOneFail(self):
        m = OneMatcher(CharCollectionMatcher([(ONE_CHAR, "a")]))
        self.assertEquals(FAIL, m.accept('b'))

    def testZeroOrMore(self):
        m = ZeroOrMoreMatcher(CharCollectionMatcher([(ONE_CHAR, "a")]))
        self.assertEquals(NEXT_CHAR, m.accept('a'))
        self.assertEquals(SKIP_MATCHER, m.accept('b'))

    def testZeroOrMore2(self):
        m = ZeroOrMoreMatcher(CharCollectionMatcher([(ONE_CHAR, "a")]))
        self.assertEquals(SKIP_MATCHER, m.accept('b'))

    def testZeroOrMore3(self):
        m = ZeroOrMoreMatcher(CharCollectionMatcher([(ONE_CHAR, "a")]))
        self.assertEquals(NEXT_CHAR, m.accept('a'))
        self.assertEquals(NEXT_CHAR, m.accept('a'))
        self.assertEquals(NEXT_CHAR, m.accept('a'))
        self.assertEquals(SKIP_MATCHER, m.accept('b'))

    def testOneOrMore(self):
        m = OneOrMoreMatcher(CharCollectionMatcher([(ONE_CHAR, "a")]))
        self.assertEquals(FAIL, m.accept('b'))

    def testOneOrMore2(self):
        m = OneOrMoreMatcher(CharCollectionMatcher([(ONE_CHAR, "a")]))
        self.assertEquals(NEXT_CHAR, m.accept('a'))
        self.assertEquals(SKIP_MATCHER, m.accept('b'))

    def testOneOrMore3(self):
        m = OneOrMoreMatcher(CharCollectionMatcher([(ONE_CHAR, "a")]))
        self.assertEquals(NEXT_CHAR, m.accept('a'))
        self.assertEquals(NEXT_CHAR, m.accept('a'))
        self.assertEquals(NEXT_CHAR, m.accept('a'))
        self.assertEquals(SKIP_MATCHER, m.accept('b'))


if __name__ == '__main__':
    unittest.main()
