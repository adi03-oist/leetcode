class Solution:
    def convertToTitle(self, n: int) -> str:
        ans=""
        while n:
            n-=1
            ans=chr(n%26+65)+ans
            n//=26
        return ans
        