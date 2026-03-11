class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s = bin(n)[2:]
        ans = ""
        for i in range(len(s)):
            temp= int(s[i])^1
            ans+=str(temp)
        return int(ans,2)          
                      
        