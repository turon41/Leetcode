class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        s = s1 + " " + s2
        ans = []
        cnt = Counter(s.split())
        for key,val in cnt.items():
            if val==1:
                ans.append(key)    
        
        return ans       


            


        