class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        for i in range(len(s)):
            minimum = len(s)

            for j in range(len(s)):
                if s[j] == c:
                    minimum = min(minimum, abs(i-j))
            ans.append(minimum)
        return ans
