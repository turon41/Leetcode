class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans =[]
        seen = {}
        cnt=0
        for i in range(n):
            if A[i] in seen:
                seen[A[i]]+=1
            else:
                seen[A[i]]=1   
            if seen[A[i]]==2:
                cnt+=1 

            if B[i] in seen:
                seen[B[i]]+=1
            else:
                seen[B[i]]=1   
            if seen[B[i]]==2:
                cnt+=1
            ans.append(cnt)
        return ans                     

        