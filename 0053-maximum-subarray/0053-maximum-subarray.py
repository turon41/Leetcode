class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxending = ans = nums[0]
        

        for i in range(1,len(nums)):
            mxending = max(mxending+nums[i],nums[i])
            ans = max(ans,mxending)

        return ans    
        