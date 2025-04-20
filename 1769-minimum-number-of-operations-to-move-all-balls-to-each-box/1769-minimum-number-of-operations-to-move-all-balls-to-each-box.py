class Solution:
    def minOperations(self, box: str) -> List[int]:
        one_ind = [i for i, val in enumerate(box) if val == "1"]
        ans = []
        for i in range(len(box)):
            sm = 0
            for num in one_ind:
                sm+= abs(num-i)
            ans.append(sm)    
        return ans
                 
        