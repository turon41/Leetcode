class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        ans = set()

        for word in words:
            odd = []
            even = []
            for i,val in enumerate(word):
                if i%2==0:
                    even.append(val)
                else:
                    odd.append(val)    
            
            odd.sort()
            even.sort()

            ans.add(''.join(odd+even))
        return len(ans)    