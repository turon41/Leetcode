class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        f,l = -1,-1
        for i in range(n):
            if nums[i]==target:
                if f==-1:
                    f=i
                l = i
        return [f,l]            
        