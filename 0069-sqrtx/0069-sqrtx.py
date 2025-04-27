class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        l,r = 1,x
        while l<=r:
            mid = (l+r)//2
            mm = (mid)*mid
            mm1 = (mid+1)*(mid+1)
            if x>=mm and x<mm1:
                return mid
            if x>mm:
                l=mid+1
            if x<mm:
                r = mid-1        
        