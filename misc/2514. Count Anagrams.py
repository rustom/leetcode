import math
class Solution:
    def countAnagrams(self, s: str) -> int:
        words = s.split()
        total = 1
        for word in words:
            letter_frequencies = [0] * 26
            for letter in word:
                letter_frequencies[ord(letter) - ord('a')] += 1
            word_total = math.factorial(len(word))
            for frequency in letter_frequencies:
                word_total //= math.factorial(frequency)
            total *= word_total

        return total % (10 ** 9 + 7)