"""
FelipedelosH
2026
"""
class PositionalEncoder:
    def __init__(self, vocabulary, synonyms, max_length=50, position_dim=8):
        self.vocabulary = vocabulary
        self.synonyms = synonyms
        self.max_length = max_length
        self.position_dim = position_dim

    def _normalize_token(self, token):
        if token in self.vocabulary:
            return {
                "original_token": token,
                "base_token": token,
                "known": True,
                "semantic_vector": self.vocabulary[token]
            }

        for base_word, synonyms_arr in self.synonyms.items():
            if token in synonyms_arr:
                if base_word in self.vocabulary:
                    return {
                        "original_token": token,
                        "base_token": base_word,
                        "known": True,
                        "semantic_vector": self.vocabulary[base_word]
                    }

        return {
            "original_token": token,
            "base_token": "UNKNOW",
            "known": False,
            "semantic_vector": None
        }

    def _build_position_vector(self, position):
        safe_position = min(position, self.max_length - 1)

        vector = []
        for i in range(self.position_dim):
            value = round((safe_position + 1) / ((i + 1) * 10), 4)
            vector.append(value)

        return vector

    def _merge_vectors(self, semantic_vector, position_vector):
        if semantic_vector is None:
            return position_vector.copy()

        return semantic_vector + position_vector

    def encode(self, tokens):
        result = []

        for index, token in enumerate(tokens):
            normalized = self._normalize_token(token)
            position_vector = self._build_position_vector(index)
            final_vector = self._merge_vectors(
                normalized["semantic_vector"],
                position_vector
            )

            result.append({
                "token": normalized["original_token"],
                "base_token": normalized["base_token"],
                "known": normalized["known"],
                "position": index,
                "position_vector": position_vector,
                "semantic_vector": normalized["semantic_vector"],
                "final_vector": final_vector
            })

        return result
