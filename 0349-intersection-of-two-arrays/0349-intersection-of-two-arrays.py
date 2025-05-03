class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        un = set()
        inter = set(nums1) & set(nums2)
        return (list(inter))

        

        