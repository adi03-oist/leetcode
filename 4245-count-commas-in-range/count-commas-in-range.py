class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0

        for i in range(1, n + 1):
            s = f"{i:,}"
            ans += s.count(",")

        return ans