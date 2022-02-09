class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
    
        if not nums:
            return 0
            
        if k< 0:
            return 0
            
        if k == 0:
            nums_dict = collections.Counter()
            for num in nums:
                nums_dict[num] += 1
            return sum(1 for val in nums_dict.values() if val > 1)
            
        nums_ = set(nums)
        return sum(1 for num in nums_ if num+k in nums_)