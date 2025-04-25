class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[0]*n
        if k==0:
            return res
        
        for i in range(n):
            if k>0:
                for j in range(i+1,i+1+k,1):
                    res[i]+=code[j%n]
            else:
                 for j in range(i-1,i-1-abs(k),-1):
                    res[i]+=code[j%n]       
        return res            