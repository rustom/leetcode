from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_of_num = defaultdict(int)
        for num in nums:
            frequency_of_num[num] += 1
        
        num_of_frequency = [[] for _ in range(len(nums) + 1)]
        for num, freq in frequency_of_num.items():
            num_of_frequency[freq].append(num)

        output = []
        for i in range(len(num_of_frequency) - 1, -1, -1):
            for num in num_of_frequency[i]:
                output.append(num)
                if len(output) >= k:
                    return output