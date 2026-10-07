class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for words in strs:
            key = ''.join(sorted(words))
            groups.setdefault(key, []).append(words)
        return list(groups.values())