from typing import List
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odds = []
        evens = []
        for element in A:
            if element % 2 == 0:
                evens.append(element)
            else:
                odds.append(element)
        return evens + odds

sol = Solution()
print(sol.sortArrayByParity([2, 3, 4, 5, 6, 7, 8, 9]))