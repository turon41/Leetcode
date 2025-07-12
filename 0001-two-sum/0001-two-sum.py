class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}

        for ind,val in enumerate(nums):
            diff = target-val
            if diff in dict_nums:
                return (dict_nums[diff],ind)

            dict_nums[val]=ind   

        

         
        