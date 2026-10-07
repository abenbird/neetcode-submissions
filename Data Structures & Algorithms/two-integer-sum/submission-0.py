class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            t = target - n
            if t in seen:
                return [seen[t], i]
            seen[n] = i
        return []