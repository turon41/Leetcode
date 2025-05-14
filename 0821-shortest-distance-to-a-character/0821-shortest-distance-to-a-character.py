class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        h = defaultdict(int)
        ans = []
        res = []
        min_dis = float("inf")
        for i,v in enumerate(s):
            if v==c:
                ans.append(i)
        for i in range(len(s)):
            for num in ans:
                cur_dis = abs(num-i)
                min_dis = min(cur_dis,min_dis)
            res.append(min_dis)
            min_dis = float("inf")
        return res    