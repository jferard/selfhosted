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
from py_tinyre.node_matcher import *
from py_tinyre.any_char_matcher import *
from py_tinyre.char_collection_matcher import *
from py_tinyre.char_collection_lexer import *

class TinyRECompiler():
    def compile(self, nodes):
        return _TinyRECompilerFor(nodes).compile()

class _TinyRECompilerFor():
    def __init__(self, nodes):
        self.__nodes = nodes

    def compile(self):
        matchers = []
        for node in self.__nodes:
            token_matcher = self.__get_token_matcher(node[VALUE])
            m = self.__get_node_matcher(node[OP_CODE], token_matcher)
            matchers.append(m)

        return matchers

    def __get_node_matcher(self, op_code, token_matcher):
        if op_code == ONE:
            m = OneMatcher(token_matcher)
        elif op_code == ZERO_OR_ONE:
            m = ZeroOrOneMatcher(token_matcher)
        elif op_code == ZERO_OR_MORE:
            m = ZeroOrMoreMatcher(token_matcher)
        elif op_code == ONE_OR_MORE:
            m = OneOrMoreMatcher(token_matcher)
        else:
            raise AssertionError("op_code="+str(op_code))
        return m


    def __get_token_matcher(self, token):
        if token[OP_CODE] == ANY_CHAR:
            return AnyCharMatcher.matcher()
        else:
            return CharCollectionMatcher(CharCollectionLexer().tokenize(token[VALUE]))
