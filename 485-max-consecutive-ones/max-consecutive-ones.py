class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxC=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                count+=1
            else:
                maxC=max(maxC,count)
                count=0
        return max(maxC,count)

        