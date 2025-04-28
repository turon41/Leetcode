class Solution:
    def strStr(self, h: str, n: str) -> int:
        if len(n)>len(h):
            return -1

        for i in range(len(h)):
            if h[i:i+len(n)]==n:
                return i
        return -1        
                  
                


        