class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        ss = set()
        for letter in s:
            if letter not in ss:
                ss.add(letter)
                print(ss)
            else:
                ss.remove(letter)
                print(ss)

        if len(ss)!=0:
            return len(s)-len(ss)+1
        else:
            return len(s)            