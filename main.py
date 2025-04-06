# main.py

import sys
from antlr4 import *
from langLexer import langLexer
from langParser import langParser
from LLVMVisitor import LLVMVisitor

def compile_lang_code(source_code):
    input_stream = InputStream(source_code)
    lexer = langLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = langParser(token_stream)
    tree = parser.prog()

    visitor = LLVMVisitor()
    module = visitor.visit(tree)
    print(module)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Użycie: python main.py <plik.lang>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        code = f.read()

    compile_lang_code(code)
