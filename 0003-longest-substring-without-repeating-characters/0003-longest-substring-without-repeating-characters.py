class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx,l = 0,0
        cnt = {}

        for ind,c in enumerate(s):
            cnt[c] = 1 + cnt.get(c,0)
            while cnt[c]>1:
                cnt[s[l]]-=1
                l+=1
            mx = max(mx,ind-l+1)    
        return mx




        