class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                if (i != nums.index(target - nums[i])):
                    return [i, nums.index(target-nums[i])]

# Accepted
# Runtime: 32 ms
# Your input
# [2,7,11,15]
# 9
# Output
# [0,1]
# Expected
# [0,1]