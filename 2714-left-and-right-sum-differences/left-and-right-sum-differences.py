class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lsum=[]
        rsum=[]
        Difference=[]
        i=0
        j=0
        for i in range(len(nums)):
            rsum.append(sum(nums[i+1:]))
        for j in range(len(nums)):
            lsum.append(sum(nums[:j]))
        for k in range(len(nums)):
            Difference.append(abs(lsum[k]-rsum[k]))
        return Difference




        