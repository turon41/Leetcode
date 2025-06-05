class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n-2):
            if nums[i]==0:
                nums[i]^=1
                nums[i+1]^=1
                nums[i+2]^=1
                cnt+=1  
        
        return cnt if (nums[n-2]==1 and nums[n-1]==1) else -1