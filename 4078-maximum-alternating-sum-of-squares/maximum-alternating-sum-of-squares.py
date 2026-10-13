class Solution:
    def maxAlternatingSum(self, nums):
        nums.sort(key=abs)

        n = len(nums)
        k = (n + 1) // 2

        small = nums[:n-k]
        big = nums[n-k:]

        ans = 0

        for i in big:
            ans += i * i

        for i in small:
            ans -= i * i

        return ans