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
from py_tinyre.char_collection_matcher import *

class TestCharCollectionMatcher(unittest.TestCase):
    def testChars(self):
        c = CharCollectionMatcher([(ONE_CHAR, 'a'),(ONE_CHAR, 'b')])
        self.assertTrue(c.match('a'))
        self.assertTrue(c.match('b'))
        self.assertFalse(c.match('c'))

    def testRange(self):
        c = CharCollectionMatcher([(CHAR_RANGE, ('a', 'z'))])
        self.assertTrue(c.match('a'))
        self.assertTrue(c.match('b'))
        self.assertTrue(c.match('z'))
        self.assertFalse(c.match('Z'))

    def testNeg(self):
        c = CharCollectionMatcher([(NEG, '\0'), (CHAR_RANGE, ('a', 'z'))])
        self.assertFalse(c.match('a'))
        self.assertFalse(c.match('b'))
        self.assertFalse(c.match('z'))
        self.assertTrue(c.match('Z'))

if __name__ == '__main__':
    unittest.main()
