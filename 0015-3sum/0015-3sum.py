class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums= sorted(nums)
        n = len(nums)
        for i in range(n-2):
            l = i+1
            r = n-1
            
            while l<r:
                temp = nums[i]+nums[l]+nums[r]
                if temp ==0:
                  ans.add((nums[i],nums[l],nums[r]))
                  l+=1
                elif temp>0:
                  r-=1
                else:
                  l+=1                
        return list(ans)