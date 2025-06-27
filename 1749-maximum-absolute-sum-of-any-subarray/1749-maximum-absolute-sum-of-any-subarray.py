class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mxending = ans = 0
        mnending = mins = 0
        
        

        for i in range(len(nums)):
            mxending = max(mxending+nums[i],nums[i])
            ans = max(ans,mxending)

            mnending = min(mnending+nums[i],nums[i])
            mins  = min(mins,mnending)

            res = max(abs(mins),abs(ans))

        return res 
        
        