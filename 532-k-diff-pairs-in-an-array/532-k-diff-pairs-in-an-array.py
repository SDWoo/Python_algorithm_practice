class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
    
        if not nums or k < 0:
            return 0
        
        if k == 0:
            nums_dict = collections.Counter()
            sum = 0
            print(nums_dict)
            for num in nums:
                nums_dict[num] += 1
            
            for val in nums_dict.values():
                if val > 1:
                   sum += 1
            return sum
        sum = 0
        my_nums = set(nums)
        for num in my_nums:
            if num+k  in my_nums:
               sum += 1
            
        return sum
            
            