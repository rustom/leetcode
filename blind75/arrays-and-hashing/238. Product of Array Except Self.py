class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        running_total = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] *= running_total
            running_total *= nums[i]

        running_total = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= running_total
            running_total *= nums[i]

        return output