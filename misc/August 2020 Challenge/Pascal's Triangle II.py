from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = []
        row.append(1)
        
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                row[j] = row[j-1] + row[j]
            row.append(1)
            
        return row

sol = Solution()
print(sol.getRow(10))