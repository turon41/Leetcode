class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxsum=minsum=0
        res = 0

        for num in nums:
            maxsum = max(maxsum,maxsum+num)

            minsum = min(num,minsum+num)
            res = max(res,abs(maxsum),abs(minsum))
        return res    

        
        
        