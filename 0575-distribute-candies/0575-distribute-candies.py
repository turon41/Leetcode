class Solution:
    def distributeCandies(self, candy: List[int]) -> int:
        n = len(candy)
        candy_s = set(candy)
        return min(n//2 , len(candy_s))

        