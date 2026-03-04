class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        n = 1<<n
        n-=1
        x = 0
        while n>1:
            if n//2 +1 ==k:
                return str(x^1)
            elif k>n//2:
                x ^= 1
                k = n-k+1
            n>>=1
        return str(x^0)
        

