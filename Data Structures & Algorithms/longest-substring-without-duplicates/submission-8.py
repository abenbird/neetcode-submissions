class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        checked = {}
        maxLen = 0
        strLen = len(s)
        while end < strLen:
            if s[end] in checked and checked[s[end]] >= start:
                lens = end - start
                start = checked[s[end]] + 1
                if lens > maxLen:
                    maxLen = lens 
            checked[s[end]] = end
            end += 1
            if end == strLen:
                lens = end - start
                if lens > maxLen:
                    maxLen = lens 
        return maxLen
            
            

