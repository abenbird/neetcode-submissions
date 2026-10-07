class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for ch in strs:
            key = ''.join(sorted(ch))
            groups.setdefault(key, []).append(ch)
        return list(groups.values())