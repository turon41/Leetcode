class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        last = nums[-1]
        lst = nums[:len(nums)-1]
        lst.sort()
        mx = (lst[-1])

        return (mx>=last or nums[mx]+mx>=last)
        