class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        for i in range(n+1):
            ans = bin(i)[2:]
            res[i]= ans.count("1")
        return res   
        