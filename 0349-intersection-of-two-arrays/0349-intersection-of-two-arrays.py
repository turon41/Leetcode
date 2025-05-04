class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2)>len(nums1):
            nums1,nums2 = nums2,nums1
        nums1.sort()
        nums2 = set(nums2) 

        ans = []
        for i in nums2:
            l,r = 0,len(nums1)-1
            while l<=r:
                mid = (l+r)//2
                val = nums1[mid]
                if val==i:
                    ans.append(i)
                    break
        
                elif val<i:
                    l = mid+1
                else:
                    r = mid-1
        return ans                     
                    

     
	   





 


        

        