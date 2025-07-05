class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,ss,mx =0,set(),0
        for i in range(len(s)):
            while s[i] in ss:
                ss.remove(s[l])
                l+=1
            ss.add(s[i])
            mx = max(mx,i-l+1) 
        return mx       



        