class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        closest_sum = 0

        nums.sort()

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            prev_distance = float('inf')

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                distance = abs(total - target)
                if distance < closest:
                    closest = distance
                    closest_sum = total
                else:
                    if total < target:
                        l += 1
                    else:
                        r -= 1
        
        return closest_sum