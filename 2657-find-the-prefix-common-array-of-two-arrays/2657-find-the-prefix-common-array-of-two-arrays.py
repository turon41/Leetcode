class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans =[0]*n
        seen = set()
        cnt=0
        for i in range(n):
            if A[i] in seen:
                cnt+=1
            else:
                seen.add(A[i])

            if B[i] in seen:
                cnt+=1
            else:
                seen.add(B[i])
            ans[i] = cnt
        return ans           

        