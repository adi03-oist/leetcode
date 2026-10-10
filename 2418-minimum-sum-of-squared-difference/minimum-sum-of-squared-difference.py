class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        
        diffs = []
        total_diff = 0
        max_diff = 0
        
        for i in range(len(nums1)):
            d = abs(nums1[i] - nums2[i])
            diffs.append(d)
            total_diff += d
            if d > max_diff:
                max_diff = d
                
        if total_diff <= k:
            return 0
        
        buckets = [0] * (max_diff + 1)
        for d in diffs:
            buckets[d] += 1
            
        for d in range(max_diff, 0, -1):
            if buckets[d] > 0:
                take = k if k < buckets[d] else buckets[d]
                buckets[d] -= take
                buckets[d - 1] += take
                k -= take
                if k == 0:
                    break
                    
        ans = 0
        for d in range(len(buckets)):
            ans += d * d * buckets[d]
            
        return ans
