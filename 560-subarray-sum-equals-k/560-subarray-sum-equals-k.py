class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        if not nums:
            return 0
        
        count = 0
        total = 0
        d = dict({0:1})
        
        for i in range(len(nums)):
            total += nums[i]
            count += d.get(total-k, 0)
            d[total] = d.get(total, 0) + 1
            
        return count