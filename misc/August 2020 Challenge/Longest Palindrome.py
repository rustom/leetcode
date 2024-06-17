class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 0:
            return 0
        counts = {}
        for letter in s:
            counts[letter] = counts.get(letter, 0) + 1
        if len(counts) == 1:
            return len(s)
        if len([count for count in counts.values() if count % 2 != 0]) <= 1:
            return len(s)
        else:
            total = 0
            oddIncluded = False
            for count in counts.values():
                if count % 2 == 0:
                    total += count
                elif not oddIncluded:
                    oddIncluded += 1
                    total += count
                else:
                    total += count - 1
            return total

sol = Solution()
print(sol.longestPalindrome('aasfdffdjjjjklfjaiiritiro'))