class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd = even =od_ev=ev_od=0
        for num in nums:
            if num&1:
                odd+=1
                od_ev = ev_od+1
            else:
                even+=1
                ev_od = od_ev+1
        return max(odd,even,ev_od,od_ev)        
    