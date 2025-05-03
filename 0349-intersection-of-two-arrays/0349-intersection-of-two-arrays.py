class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2)>len(nums1):
            nums1,nums2 = nums2,nums1
            

        ans=[]    
        for i in nums1:
            if i in nums2:
                ans.append(i)

        return (list(set(ans)))
        

        