class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        h = defaultdict(int)
        for num in nums:
            h[num]+=1
        s = 0    
        for key,val in h.items():
            if val>2:
                while (val-2)!=s:
                    nums.remove(key) 
                    s+=1
                s=0
                continue
        return len(nums)                           
        