class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        Counter = collections.Counter(nums)
        
        result = Counter.most_common(1)[0][0]
        return result