class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        nums_set = set(nums)
        max_length = 0
        for num in nums_set:
            if num - 1 not in nums_set: 
                length = 1
                while num + 1 in nums_set:
                    length += 1
                    num += 1
                max_length = max(length, max_length)

        return max_length
