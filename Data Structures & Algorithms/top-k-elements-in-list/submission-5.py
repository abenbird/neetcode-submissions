class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        buckets = []
        bucketsLen = len(nums) + 1
        while bucketsLen > 0:
            buckets.append([])
            bucketsLen -= 1
        
        for c, n in count.items():
            buckets[n].append(c)
        
        result = []
        freq = len(buckets) - 1
        while freq >= 0:
            for n in buckets[freq]:
                result.append(n)
                if len(result) == k:
                    return result
            freq -= 1
        return result