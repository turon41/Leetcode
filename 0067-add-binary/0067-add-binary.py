class Solution:
    def addBinary(self, a: str, b: str) -> str:
        adec = int(a,2)
        bdec = int(b,2)
        ans = adec+bdec
        return format(ans,'b')
        