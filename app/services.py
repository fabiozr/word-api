from typing import List


class WordService:
    def count_vowels(self, words: List[str]) -> dict:
        vowels = "aeiou"
        return {
            word: sum(1 for char in word.lower() if char in vowels) for word in words
        }

    def sort_words(self, words: List[str], order: str) -> List[str]:
        return sorted(words, key=str.lower, reverse=(order.lower() == "desc"))
