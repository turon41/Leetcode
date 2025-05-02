class Solution:
    def shortestCompletingWord(self, l: str, words: List[str]) -> str:
        lt = Counter(ltr.lower() for ltr in l if ltr.isalpha())

        return min((w for w in words if not lt - Counter(w)),key=len)

        