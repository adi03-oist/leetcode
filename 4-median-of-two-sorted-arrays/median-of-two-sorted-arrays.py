class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=nums1+nums2
        arr.sort()
        n=len(arr)
        if n %2==0:
            t=arr[n//2]  + arr[n//2-1]
            m=t/2
        else:
            t=n//2
            m=arr[t]
        return m
       
        