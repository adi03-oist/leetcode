class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        n = len(nums)

        max_index = nums.index(max(nums))
        min_index = nums.index(min(nums))

        left = max(max_index, min_index) + 1

        right = n - min(max_index, min_index)

        both = min(max_index, min_index) + 1 + n - max(max_index, min_index)

        return min(left, right, both)