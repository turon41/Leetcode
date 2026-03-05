class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol,res = [],[]
        n = len(nums)
        def backtrack(i):
            if i==n:
                res.append(sol[:])
                return

            

            # pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            # Don't pick nums[i]
            backtrack(i+1) 

        backtrack(0)      
        return res