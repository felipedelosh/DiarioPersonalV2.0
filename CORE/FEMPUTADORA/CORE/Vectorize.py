"""
FelipedelosH
2026

Enter arr of tokens and return [x,y,...z]
"""
class Vectorizer:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        
    def vectorize(self, arrTokens):
        dimensions = len(next(iter(self.vocabulary.values())))
        vector = [0] * dimensions

        for token in arrTokens:
            if token in self.vocabulary:
                token_vec = self.vocabulary[token]
                vector = [max(a, b) for a, b in zip(vector, token_vec)]

        return vector
 