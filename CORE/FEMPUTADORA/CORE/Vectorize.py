"""
FelipedelosH
2026

Enter arr of tokens and return [x,y,...z]

if pivot == 1 position be 1
else sum
if sum > 1 position be 1
else be sum
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
                new_vector = []

                for current_value, found_value in zip(vector, token_vec):
                    if found_value == 1:
                        new_vector.append(1)
                    else:
                        summed_value = current_value + found_value
                        if summed_value > 1:
                            summed_value = 1
                        new_vector.append(summed_value)

                vector = new_vector

        return vector
 