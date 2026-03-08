class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        s = set(nums)
        for i in range(1<<n):
            temp = format(i,f"0{n}b")
            if temp not in s:
                return temp


       




        