class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_index = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen_index:
                return [i, seen_index[complement]]
            seen_index[nums[i]] = i
