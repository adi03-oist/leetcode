class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[]

        for i in range(n):
            index = (i+nums[i])%n
            result.append(nums[index])
        return result
