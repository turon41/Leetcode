class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res =[]
        nums = set(nums)
        for i in range(1,n+1):
            if i not in nums:
                res.append(i)
        return res
        