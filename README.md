# Self Hosted - A Self Hosted compiler project

Copyright (C) 2017 J. Férard <https://github.com/jferard>

This is an experimental project, and a work in progress.

**Do not rely on it.**

## The project
I will try to make a tiny self hosted compiler, one part after another.
The goal is to create in Python a compiler based on LLVM.
This compiler should be able to compile itself.

The only requirements will be:
- LLVM
- a python 3 interpreteter
- python llvmlite module

## Roadmap
There are two main steps : the bootstrap in Python, and the self hosted compiler.

### The bootstrap
1. Create a tiny regex library in Python
2. Create a lexer on tiny regexes
3. Create a parser on BNF & lexer
4. Use the previous steps to output an executable build on LLVM

### The self hosted compiler
1. Translate Python sources to self hosted syntax.
2. Tie this to LLVM

See https://github.com/jferard/selfhosted/ROADMAP.md
