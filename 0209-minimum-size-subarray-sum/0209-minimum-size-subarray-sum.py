class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,sm,mn = 0,0, float('inf')
        for i in range(len(nums)):
            sm+=nums[i]
            while sm>=target:
                mn = min(mn,i-l+1)
                sm-=nums[l]
                l+=1
        return 0 if mn==float('inf') else mn
        