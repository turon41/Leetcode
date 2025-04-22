class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ans = []
        for i in s:
           if i.isalnum(): ans.append(i)
        
        return ans==ans[::-1]