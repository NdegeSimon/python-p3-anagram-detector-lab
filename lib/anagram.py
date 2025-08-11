# lib/anagram.py

class Anagram:
    def __init__(self, word):
        # Store the original word in lowercase for consistent comparison
        self.word = word.lower()

    def match(self, candidates):
        matches = []
        sorted_word = sorted(self.word)

        for candidate in candidates:
            cand_lower = candidate.lower()
            if cand_lower != self.word and sorted(cand_lower) == sorted_word:
                matches.append(candidate)

        return matches
