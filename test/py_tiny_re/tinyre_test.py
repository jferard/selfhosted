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
from py_tinyre import *

class TestTinyRE(unittest.TestCase):
    def testPattern(self):
        re = TinyRE("[p][a][t][t][e][r][n]")
        self.assertEquals(NEXT_CHAR, re.accept("p"))
        self.assertEquals(NEXT_CHAR, re.accept("a"))
        self.assertEquals(NEXT_CHAR, re.accept("t"))
        self.assertEquals(NEXT_CHAR, re.accept("t"))
        self.assertEquals(NEXT_CHAR, re.accept("e"))
        self.assertEquals(NEXT_CHAR, re.accept("r"))
        self.assertEquals(NEXT_CHAR, re.accept("n"))
        self.assertEquals(SUCCESS, re.accept("\0"))

    def testPattern2(self):
        re = TinyRE("[p][a][t][t][e][r][n]")
        self.assertEquals(NEXT_CHAR, re.accept("p"))
        self.assertEquals(NEXT_CHAR, re.accept("a"))
        self.assertEquals(NEXT_CHAR, re.accept("t"))
        self.assertEquals(FAIL, re.accept("s"))

    def testPatternPlus(self):
        re = TinyRE("[p][a][t]+")
        self.assertEquals(NEXT_CHAR, re.accept("p"))
        self.assertEquals(NEXT_CHAR, re.accept("a"))
        self.assertEquals(NEXT_CHAR, re.accept("t"))
        self.assertEquals(NEXT_CHAR, re.accept("t"))
        self.assertEquals(NEXT_CHAR, re.accept("t"))
        self.assertEquals(NEXT_CHAR, re.accept("t"))
        self.assertEquals(SUCCESS, re.accept("e"))

if __name__ == '__main__':
    unittest.main()
