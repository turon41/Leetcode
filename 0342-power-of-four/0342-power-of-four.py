class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1: return True
        if n%4==0:
            while n:
                n//=4
            return True    
        return False