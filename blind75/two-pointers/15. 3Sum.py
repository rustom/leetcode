class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    triplet = [nums[i], nums[l], nums[r]]
                    output.append(triplet)
                    while l < len(nums) and nums[l] == triplet[1]:
                        l += 1
                    while r > 0 and nums[r] == triplet[2]:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return output