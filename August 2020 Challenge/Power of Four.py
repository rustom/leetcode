import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        else:
            return math.log(num, 4).is_integer()

sol = Solution()
print(sol.isPowerOfFour(67108864))