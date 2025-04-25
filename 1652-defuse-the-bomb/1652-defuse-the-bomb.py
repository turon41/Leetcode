class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        for r in range(len(code)):
            print(code[r+1:k])