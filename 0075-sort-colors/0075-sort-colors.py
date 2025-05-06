class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        h = defaultdict(int)
        for num in nums:
            h[num]+=1
        ind = 0    
        for i in range(3):
            while h[i]>0:
                nums[ind]=i
                ind+=1
                h[i]-=1


            
        