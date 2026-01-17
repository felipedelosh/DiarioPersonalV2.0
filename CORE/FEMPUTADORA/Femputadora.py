"""
FelipedelosH
2026
"""
from CORE.FEMPUTADORA.CORE.vocabulary_tokenizer_ids import vocabulary
from CORE.FEMPUTADORA.CORE.Tokenizer import Tokenizer

class Femputadora:
    def __init__(self):
        self.vocabulary = vocabulary
        self.Tokenizer = Tokenizer()

    def getResponse(self, text):
        # STEP 01: GET TOKENS
        tokens = self.Tokenizer.tokenize(text)

        print("TOKEN ARR: ")
        print(tokens)

        return "Powered in Future By FelipedelosH"
    
