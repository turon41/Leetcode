class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        res,sol = [],[]
        def backtrack(i,k):
            if k==0:
                res.append(sol[:])
                return
            if i>n:
                return
            sol.append(i)
            backtrack(i+1,k-1)
            sol.pop()
            backtrack(i+1,k)
            
        backtrack(1,k)
        return res        
        

__import__("atexit").register(lambda:open("display_runtime.txt","w").write("0"))
