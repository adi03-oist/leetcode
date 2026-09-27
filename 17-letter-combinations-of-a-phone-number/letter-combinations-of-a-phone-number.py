class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []
        phone ={
            "2" :"abc",
            "3" :"def",
            "4" :"ghi",
            "5" :"jkl",
            "6" :"mno",
            "7" :"pqrs",
            "8" :"tuv",
            "9" :"wxyz"

        }

        ans = [""]

        for digit in digits:
            temp = []

            for i in ans:
                for j in phone[digit]:
                    temp.append(i + j)
                    ans = temp
        return ans
            

        
        