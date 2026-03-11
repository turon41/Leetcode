class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        if n==0:
            return 1
        ln = n.bit_length()
        temp = (1<<ln)-1
        return n^temp         
                      
        