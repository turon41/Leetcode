class Solution:
    def distributeCandies(self, candy: List[int]) -> int:
        h= defaultdict(int)
        for c in candy:
            h[c]+=1
        return min(len(h),len(candy)//2)   

         

        