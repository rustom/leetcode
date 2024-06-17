class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for string in strs:
            output += str(len(string)) + '#' + string
        return output

    def decode(self, s: str) -> List[str]:
        output = []

        l, r = 0, 0
        while l < len(s):
            while s[r] != '#':
                r += 1
            string_len = int(s[l:r])
            output.append(s[r + 1:r + 1 + string_len])
            l = r + 1 + string_len
            r = l

        return output