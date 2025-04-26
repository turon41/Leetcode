class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sm = sum(nums)
        lsum = [0]*n
        rsum = [0]*n
        ans = [0]*n
        for i in range(1,n):
            lsum[i]= lsum[i-1]+nums[i-1]
            rsum[i-1] = sm-nums[i-1]
            sm-=nums[i-1]
        for i in range(n):
            ans[i] = abs(lsum[i]-rsum[i])    
        return ans

         