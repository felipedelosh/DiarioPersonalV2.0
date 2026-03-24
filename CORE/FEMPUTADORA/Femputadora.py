"""
FelipedelosH
2026
"""
from CORE.FEMPUTADORA.CORE.vocabulary_tokenizer_ids import vocabulary
from CORE.FEMPUTADORA.CORE.synonimyzer import synonyms
from CORE.FEMPUTADORA.CORE.Tokenizer import Tokenizer
from CORE.FEMPUTADORA.CORE.Vectorize import Vectorizer
from CORE.FEMPUTADORA.CORE.positional_encoder import PositionalEncoder

class Femputadora:
    def __init__(self):
        self.vocabulary = vocabulary
        self.synonyms = synonyms
        self.Tokenizer = Tokenizer()
        self.Vectorizer = Vectorizer(self.vocabulary, self.synonyms)
        self.PositionalEncoder = PositionalEncoder(self.vocabulary, self.synonyms)

        # VARS
        self._chatCounter = 0 # times to user INPUT txt

    def getResponse(self, text):
        # STEP 01: GET TOKENS
        tokens = self.Tokenizer.tokenize(text)

        # STEP 02: Vectorize
        vector = self.Vectorizer.vectorize(tokens)

        # STEP 03: Positional Encoder
        positional_data = self.PositionalEncoder.encode(tokens)


        # ...
        self._chatCounter = self._chatCounter + 1

        return {
            "chat_counter": self._chatCounter,
            "tokens": tokens,
            "vector": vector,
            "positional_data": positional_data
        }
