class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(mat)
        for i in range(n):
            for j in range(i+1,n):
                mat[i][j], mat[j][i] = mat[j][i],mat[i][j]
        
        for i in range(n):
            for j in range(n//2):
                mat[i][j],mat[i][n-j-1] = mat[i][n-j-1], mat[i][j]           