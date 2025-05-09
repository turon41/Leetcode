class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 0
        while ind<len(nums):
            if nums.count(nums[ind])>2:
                nums.remove(nums[ind])
            else:
                ind+=2
        return len(nums)            
                     

