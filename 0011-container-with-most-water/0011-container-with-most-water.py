class Solution:
    def maxArea(self, a: List[int]) -> int:
        l = 0
        r= len(a)-1
        mx_h = max(a)
        mx = 0
        while l<r:
            if mx_h*(r-l)<mx:
                return mx

            w = min(a[l],a[r])
            mx = max(mx,w*(r-l))
            if a[l]<a[r]:
                l+=1
            else:
                r-=1
        return mx            

        