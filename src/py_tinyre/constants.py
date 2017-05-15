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

# lexer state
START = 0
AFTER_CHAR = 1
GOBBLE_CHAR = 2

OP_CODE = 0
VALUE = 1

# tokens opcode
ANY_CHAR = 10
CHAR_COLLECTION = 20
GLOB = 30

# char collection parser
NEG = 0
ONE_CHAR = 100
CHAR_RANGE = 200

# parser
ONE = 1
ZERO_OR_ONE = 2
ZERO_OR_MORE = 3
ONE_OR_MORE = 4

# compiler
FAIL = 0
SKIP_MATCHER = 2
NEXT_MATCHER_AND_CHAR = 3
NEXT_CHAR = 4
SUCCESS = 5
