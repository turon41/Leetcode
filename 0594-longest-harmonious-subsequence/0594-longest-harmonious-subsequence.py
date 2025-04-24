class Solution:
    def findLHS(self, nums: List[int]) -> int:
        l,r=0,1
        mx = 0
        nums.sort()
        while r<(len(nums)):
            diff = nums[r]-nums[l]
            if diff==1:
                mx = max(mx,r-l+1)
            if diff<=1:
                r+=1
            else:
                l+=1        
        return mx       


        