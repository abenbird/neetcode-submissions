class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        buckets = []
        for _ in range(len(nums) + 1):
            buckets.append([])
        for c, n in count.items():
            buckets[n].append(c)
        
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for n in buckets[freq]:
                result.append(n)
                if len(result) == k:
                    return result
        return result