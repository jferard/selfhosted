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
from py_tinyre.tinyre_matcher import TinyREMatcher

class TestTinyREMatcher(unittest.TestCase):
    def testOneOK(self):
        matchers = [OneMatcher(CharCollectionMatcher([(ONE_CHAR, "a")]))]
        t = TinyREMatcher(matchers)
        self.assertEquals(SUCCESS, t.accept("a"))

    def testOneOK2(self):
        matchers = [
            OneMatcher(CharCollectionMatcher([(ONE_CHAR, l)])) for l in "pattern"
        ]
        t = TinyREMatcher(matchers)
        for l in "patter":
            self.assertEquals(NEXT_CHAR, t.accept(l))
        self.assertEquals(SUCCESS, t.accept("n"))


    def testOneFail(self):
        matchers = [OneMatcher(CharCollectionMatcher([(ONE_CHAR, "a")]))]
        t = TinyREMatcher(matchers)
        self.assertEquals(FAIL, t.accept("b"))

    def testZeroOrMoreOK(self):
        matchers = [ZeroOrMoreMatcher(CharCollectionMatcher([(ONE_CHAR, "a")]))]
        t = TinyREMatcher(matchers)
        self.assertEquals(NEXT_CHAR, t.accept("a"))
        self.assertEquals(NEXT_CHAR, t.accept("a"))
        self.assertEquals(NEXT_CHAR, t.accept("a"))
        self.assertEquals(SUCCESS, t.accept("b"))

    def testZeroOrMoreFail(self):
        matchers = [ZeroOrMoreMatcher(CharCollectionMatcher([(ONE_CHAR, "a")]))]
        t = TinyREMatcher(matchers)
        self.assertEquals(SUCCESS, t.accept("b"))

if __name__ == '__main__':
    unittest.main()
