class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):

            left = nums[:i+1]
            right = nums[i:]

            maximum = max(left)
            minimum = min(right)

            if maximum - minimum <= k:
                return i

        return -1