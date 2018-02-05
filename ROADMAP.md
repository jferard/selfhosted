# ROADMAP (WORK IN PROGRESS)
There are two main steps : the bootstrap compiler in Python, and the self hosted compiler.

## Goal
The goal is an executable program that compiles a source written in SelfHosted (a C-like language) and generates a LLVM IR. This LLVM IR may be compiled to an executable.
This executable is generated from a LLVM IR source, and this LLVM IR source is generated:
* from a Python source (bootstrap)
* from a SelfHosted source (SelfHosted compiler).

## References
* The LLVM documentation: https://llvm.org/docs/LangRef.html

## The bootstrap
Python and llvmlite.

### The lexer
#### References:
* https://algs4.cs.princeton.edu/54regexp/NFA.java.html
* Sedgewick, *Algorithms in C*, p. 293 sqq
* *Dragon Book*, p. 116 sqq
* https://www.tutorialspoint.com/automata_theory/index.htm

#### Steps
* Create in Python + llvmlite a LLVM-IR program that converts a subset of regexes into a NFA.
* Create in Python + llvmlite a LLVM-IR program that converts a NFA into a DFA.
* Given a language specification (pattern - action written in Python), build in Python + llvmlite a LLVM-IR source for a lexer.

### The parser
#### References:
* *Dragon Book*, p. 233 sqq

#### Steps
* Given a BNF set of rules (with semantic actions associated), build in Python + llvmlite a LLVM-IR source for a parser.

At this point, we have a LLVM-IR program that takes any (very simple) token definition and grammar and outputs a basic compiler in LLVM-IR.

## The self hosted compiler
* Given a SelfHosted grammar, create a basic SelfHosted compiler
* Adapt llvmlite to SelfHosted
* Convert the Python + llvmlite sources to SelfHosted + llvmlite sources.
