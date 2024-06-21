from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen = set()
        l, r = 0, 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                
            seen.add(s[r])
            r += 1

            max_len = max(max_len, len(seen))
        return max_len

