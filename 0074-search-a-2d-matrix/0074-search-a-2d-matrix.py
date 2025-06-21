class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j]==target:
                    return True
        return False
        