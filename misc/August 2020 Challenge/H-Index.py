class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        citations.sort()
        for i in range(len(citations)):
            opp = len(citations) - i
            if citations[i] >= opp and (i < 1 or citations[i - 1] <= opp):
                h = max(h , opp)
            
        return h

