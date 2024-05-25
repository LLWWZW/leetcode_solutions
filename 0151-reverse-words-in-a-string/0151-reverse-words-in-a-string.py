class Solution:
    def reverseWords(self, s: str) -> str:
        store_words = s.split()
        store_words.reverse()

        return " ".join(store_words)