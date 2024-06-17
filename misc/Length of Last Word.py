class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip()
        pieces = string.split(' ')
        try:
            return len(pieces[-1])
        except:
            return 0

sol = Solution()
print(sol.lengthOfLastWord('a '))