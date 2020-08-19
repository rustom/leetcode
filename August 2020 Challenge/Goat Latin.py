class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        words = S.split()
        for i in range(len(words)):
            if words[i][0].lower() in vowels:
                words[i] += 'ma'
            else:
                first = words[i][0]
                words[i] = words[i][1:] + first + 'ma'
            words[i] += 'a' * (i + 1)
        return ' '.join(words)

sol  = Solution()
sol.toGoatLatin('Are you sure this is right?')