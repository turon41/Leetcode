class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol,res = [],[]
        n = len(nums)
        def backtrack(i):
            
            res.append(sol[:])

            for j in range(i,n):
                sol.append(nums[j])                       # pick nums[i]
                backtrack(j+1)          
                sol.pop()

            # # Don't pick nums[i]
            # backtrack(i+1)     #it happens through the loop

        backtrack(0)      
        return res