class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        mx = -1

        for ind,val in cnt.items():
            if ind==val:
                mx = max(mx,val)
        return mx   
        