class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        n = len(nums)
        pos = []
        neg = []
        for i in nums:
            if i==0:
                return 0
            elif i<0:
                neg.append(i)
            else:
                pos.append(i)

        if not pos:
            return max(neg)
        if not neg:
            return min(pos)
        
        if abs(min(pos))<=abs(max(neg)):
            return min(pos)
        else:
            return max(neg)    
                    

        