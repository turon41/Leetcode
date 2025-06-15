class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3: return n

        p2=2
        p1 = 3
        temp=0

        for i in range(3,n):
            temp = p1+p2
            p2  = p1
            p1 = temp

        return p1
         
                
    
        
        