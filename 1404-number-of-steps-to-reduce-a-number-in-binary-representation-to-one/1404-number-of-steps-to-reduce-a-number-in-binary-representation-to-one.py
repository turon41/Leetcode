class Solution:
    def numSteps(self, s: str) -> int:
        ans = int(s,2)

        cnt=0
        while ans!=1:
            if ans%2:
                ans+=1
                cnt+=1

            elif ans%2==0 and ans & (ans-1)==0:
                cnt+=int(log2(ans))
                break
            else:
                ans//=2
                cnt+=1
        return cnt              


            
        