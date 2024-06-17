class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_total = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            running_total = 1
            current = num + 1
            while current in nums_set:
                current += 1
                running_total += 1
            max_total = max(max_total, running_total)
        return max_total