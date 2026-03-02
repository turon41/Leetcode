class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = []
        for row in grid:
            cnt=0
            for i in range(n-1,-1,-1):
                if row[i]==0:
                    cnt+=1
                else:
                    break    
            zeros.append(cnt)          
        steps = 0

        for i in range(n):
            need = n-i-1
            j=i
            while j<n and zeros[j]<need:
                j+=1

            if j==n: return -1
            steps+=(j-i)
            while j>i:
                zeros[j], zeros[j-1] = zeros[j-1], zeros[j]
                j-=1
                #steps+=1
        return steps            
        