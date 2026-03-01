class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums[:]]
        n = len(nums)    
        res,sol = [], []    
        
        def backtrack():
            if len(sol)==n:
                res.append(sol[:])
                return
            for e in nums:
                if e not in sol:
                    sol.append(e)
                    backtrack()
                    sol.pop()
        backtrack()
        return res                  
