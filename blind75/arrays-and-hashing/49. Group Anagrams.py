from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for string in strs:
            letter_frequencies = [0] * 26
            for letter in string:
                letter_frequencies[ord(letter) - ord('a')] += 1
            counts[tuple(letter_frequencies)].append(string)
        return counts.values()