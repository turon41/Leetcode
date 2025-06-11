class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res = Counter(nums)
        ans = 0
        for ind,val in res.items():
            if val>1:
                ans = ans^ind

        return ans