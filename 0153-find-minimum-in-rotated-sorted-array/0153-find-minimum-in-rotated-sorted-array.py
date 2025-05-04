class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 0,len(nums)-1
        
        val = nums[0]
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>val:
                r = mid-1
            elif nums[mid]<val:
                l = mid+1
            else:
                return val
                        
            
        
        