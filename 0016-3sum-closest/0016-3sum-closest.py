class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n  = len(nums)
        close = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            l = i+1
            r = n-1

            while l<r:
                cursum = (nums[i]+nums[l]+nums[r])
                if cursum==target:
                    return target
                if abs(target-cursum)< abs(target-close):
                    close = cursum
                
                if target>cursum:
                    l+=1
                else:
                    r-=1  
        return close                  

                 
                 

        