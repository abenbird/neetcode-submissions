class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s1Len = len(s1)
        for i in range(len(s2)):
            subStr = s2[i: i + s1Len]
            subStr = sorted(subStr)
            if s1 == subStr:
                return True
        return False