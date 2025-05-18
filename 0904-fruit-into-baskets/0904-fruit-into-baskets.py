class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(set(fruits))==2:
            return len(fruits)
        
        h = defaultdict(int)
        l,mx = 0,0
        for right in range(len(fruits)):
            h[fruits[right]]+=1
            
            while len(h)>2:
                h[fruits[l]]-=1
                if h[fruits[l]]==0:
                    del h[fruits[l]]
                l+=1    
            
            mx = max(mx,right-l+1)
        return mx