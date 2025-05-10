class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        l,r=0,0
        ans = []
        while l<len(fl) and r<len(sl):
            i1 = fl[l]
            i2 = sl[r]

            s = max(i1[0],i2[0])
            e = min(i1[1],i2[1])

            if s<=e:
                ans.append([s,e])
            if i1[1]<i2[1]:
                l+=1
            else:
                r+=1
        return ans                


        
