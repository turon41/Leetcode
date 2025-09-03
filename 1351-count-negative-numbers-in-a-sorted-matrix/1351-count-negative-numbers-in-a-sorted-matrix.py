class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg=0
        for m in grid:
            for n in m:
                if n<0:
                    neg+=1
        return neg