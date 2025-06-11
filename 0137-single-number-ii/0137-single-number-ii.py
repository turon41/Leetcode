class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for ind,val in cnt.items():
            if val==1:
                return ind
        