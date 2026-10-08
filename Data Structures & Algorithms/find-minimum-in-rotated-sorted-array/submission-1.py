class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        mins = nums[l]
        while l <= r:
            k = int((l + r) / 2)
            if nums[k] <= nums[r]:
                mins = min(mins, nums[k])
                r = k - 1
            else:
                l = k + 1
        return mins

            
