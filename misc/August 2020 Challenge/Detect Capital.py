class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if word[0].isupper():
            if word[1:len(word)].islower():
                return True
            elif word[1:len(word)].isupper():
                return True
            else:
                return False
        else:
            if word[1:len(word)].islower():
                return True
            else:
                return False
        
sol = Solution()
print(sol.detectCapitalUse("USA"))