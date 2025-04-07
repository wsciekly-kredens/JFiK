import sys
from antlr4 import *
from langLexer import langLexer
from langParser import langParser
from LLVMVisitor import LLVMVisitor
from langErrorListener import LangErrorListener

def compile_lang_code(source_code):
    input_stream = InputStream(source_code)

    lexer = langLexer(input_stream)
    lexer.removeErrorListeners()
    lexer_error_listener = LangErrorListener()
    lexer.addErrorListener(lexer_error_listener)

    token_stream = CommonTokenStream(lexer)

    parser = langParser(token_stream)
    parser.removeErrorListeners()
    parser_error_listener = LangErrorListener()
    parser.addErrorListener(parser_error_listener)

    tree = parser.prog()

    if lexer_error_listener.has_errors or parser_error_listener.has_errors:
        print("Wystąpiły błędy leksykalne lub składniowe. Kompilacja przerwana.")
        return

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
