class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(set(fruits))==2:
            return len(fruits)
        
        h = defaultdict(int)
        l,mx = 0,0
        for right in range(len(fruits)):
            h[fruits[right]]=right
            
            if len(h)>2:
                min_ind = min(h.values())
                l = min_ind+1
                del h[fruits[min_ind]]
            mx = max(mx,right-l+1)     

        return mx