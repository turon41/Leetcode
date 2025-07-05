class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        a = [i for i in range(0,n+1)]

        

        for num in a:
            if num not in nums:
                return num
                break
        
        