class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 0
        mod = 10**9 + 7
        for i in range(1,n+1):
            ans = len(bin(i))-2
            res = (res<<ans | i) %mod
        return res    
            

        