class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in reversed(range(len(s))):
            num += (alphabet.index(s[i]) + 1) * (26 ** (len(s) - i - 1))
        return num


sol = Solution()
print(sol.titleToNumber('AB'))