from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums: nums.remove(val)
        return len(nums)

sol = Solution()
print(sol.removeElement([1, 2, 3, 3, 3, 2, 1, 2], 2))