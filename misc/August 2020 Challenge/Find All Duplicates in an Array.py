from typing import List
class Solution: 
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[nums[i] % len(nums)] += len(nums)
        results = []
        for index, value in enumerate(nums):
            if value > 2 * len(nums):
                if index == 0:
                    results.append(len(nums))
                else:
                    results.append(index)
        return results
sol = Solution()
print(sol.findDuplicates([2, 3, 2, 4, 5, 5, 5, 6, 7, 7, 9]))