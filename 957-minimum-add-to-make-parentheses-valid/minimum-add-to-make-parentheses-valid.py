class Solution:
    def minAddToMakeValid(self, s):
        count = 0
        ans = 0

        for ch in s:
            if ch == "(":
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    ans += 1

        return ans + count