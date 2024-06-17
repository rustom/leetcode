import re
class Solution: 
    def isPalindrome(self, s: str) -> bool:
        bare = ''.join([str(letter) for letter in s if letter.isalnum()])
        bare = bare.lower()
        if len(bare) == 1: 
            return True
        if len(bare) % 2 != 0:
            middle = len(bare) // 2
            bare = bare[:middle] + bare[middle + 1:]
        if bare[::-1] == bare:
            return True
        else:
            return False

sol = Solution()
print(sol.isPalindrome("A man, a plan, a Canal: Panama"))