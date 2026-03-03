class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n==1:
            return "0"
        l = (1<<n) -1
        mid = l//2 +1

        if k==mid:
            return "1"
        elif k<mid:
            return self.findKthBit(n-1,k)
        else:
            mirror = l-k+1
            bit = self.findKthBit(n-1,mirror) 
            return "1" if bit=="0" else "0" 

        