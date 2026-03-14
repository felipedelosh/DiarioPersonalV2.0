"""
FelipedelosH
2026

Enter arr of tokens and return [x,y,...z]
"""
class Vectorizer:
    def __init__(self, vocabulary, synonyms):
        self.vocabulary = vocabulary
        self.synonyms = synonyms
        
    def vectorize(self, arrTokens):
        dimensions = len(next(iter(self.vocabulary.values())))
        vector = [0] * dimensions

        for token in arrTokens:
            token_vec = None

            if token in self.vocabulary:
                token_vec = self.vocabulary[token]
            else:
                for base_word, synonyms_arr in self.synonyms.items():
                    if token in synonyms_arr:
                        if base_word in self.vocabulary:
                            token_vec = self.vocabulary[base_word]
                            break

            if token_vec is not None:
                vector = [max(a, b) for a, b in zip(vector, token_vec)]

        return vector
 