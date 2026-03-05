class Solution:
    def minOperations(self, s: str) -> int:
        cnt,n = 0, len(s)

        for i in range(n):
            if i%2: #Odd
                cnt+=1 if s[i]=="0" else 0
            else: #even
                cnt+=1 if s[i]=="1" else 0    
               
        return min(cnt,n-cnt)    

                
