class Solution:
    def maxScore(self, s: str) -> int:
        prefixSum = [0]
        for c in s:
            prefixSum.append(prefixSum[-1]+int(c))
        if len(s) == 2:
            return prefixSum[-1]+1
        maxScore = 0
        for i in range(1,len(s)-1):
            maxScore = max(maxScore,(i+1-prefixSum[i])+(prefixSum[-1]-prefixSum[i+1]))
        
        return maxScore