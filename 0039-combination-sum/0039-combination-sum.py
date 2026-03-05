class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol = [],[]
        nums = candidates
        n = len(nums)

        def backtrack(i,cur_sum):
            if cur_sum==target:
                res.append(sol[:])
                return
            if cur_sum>target or i==n:
                return

            for j in range(i,n):
                sol.append(nums[j])
                backtrack(j,cur_sum+nums[j])
                sol.pop()

            #backtrack(i+1,cur_sum)  #don't pick
        backtrack(0,0)
        return res          


