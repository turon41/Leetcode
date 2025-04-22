class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ans = ""
        for i in s:
           if ord(i)<=122 and ord(i)>=97: ans+=i
        
        return ans==ans[::-1]