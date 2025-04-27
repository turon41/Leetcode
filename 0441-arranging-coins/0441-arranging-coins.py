class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 1,n
        while l<=r:
            mid = (r+l)//2
            if n>=(mid)*(mid+1)//2:
                l=mid+1
            else:
                r=mid-1
        return r            
             
        