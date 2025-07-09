class Solution:
    def maxFreeTime(self, event: int, k: int, start: List[int], end: List[int]) -> int:
        n = len(start)
        gaps = [0]*(n+1)

        gaps[0] = start[0]
        gaps[n]  = event- end[-1]

        for i in range(1,n):
            gaps[i] = start[i]-end[i-1]

        window = sum(gaps[:k+1]) 
        res =window

        for i in range(k+1,n+1):
            window = window- (gaps[i-(k+1)]) + gaps[i]
            res = max(res,window)
        return res    



        