class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        counts = []
        for word in words:
            letter_frequencies = [0] * 26
            for letter in word:
                letter_frequencies[ord(letter) - ord('a')] += 1

            counts.append(tuple(letter_frequencies))
        
        output = []
        l, r = 0, 0
        while l < len(counts):
            output.append(words[l])
            while r < len(counts) and counts[r] == counts[l]:
                r += 1
            l = r
        return output