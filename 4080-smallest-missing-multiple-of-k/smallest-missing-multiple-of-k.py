class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiple = k
        nums=set(nums)
        while True:
            if multiple not in nums:
                return multiple
            multiple += k
            

        