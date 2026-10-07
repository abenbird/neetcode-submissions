class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)

        maxlen = 0
        checked = set()
        for n in snums:
            if n in checked:
                continue
            checked.add(n)
            sequence = 1
            left = n - 1
            while left in snums:
                checked.add(left)
                sequence += 1
                left -= 1
            right = n + 1
            while right in snums:
                checked.add(right)
                sequence += 1
                right += 1
            if sequence > maxlen:
                maxlen = sequence
        return maxlen
            
