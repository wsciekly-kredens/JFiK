from antlr4.error.ErrorListener import ErrorListener

class LangErrorListener(ErrorListener):
    def __init__(self):
        super(LangErrorListener, self).__init__()
        self.has_errors = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_errors = True
        print(f"[BŁĄD składni] Linia {line}, kolumna {column}: {msg}")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print(f"[Ostrzeżenie] Niejednoznaczność od {startIndex} do {stopIndex}")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print(f"[Debug] Przełączanie do pełnego kontekstu od {startIndex} do {stopIndex}")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print(f"[Debug] Wrażliwość kontekstu od {startIndex} do {stopIndex}")
