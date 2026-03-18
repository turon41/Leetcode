# Added using AI
class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        grid = map(accumulate,grid)
        grid = map(accumulate,zip(*grid))

        return sum(val<=k for row in grid for val in row)