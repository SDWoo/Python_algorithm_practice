class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        deque = collections.deque()
        
        for i,n in enumerate(nums):
            while deque and nums[deque[-1]] <= n:
                deque.pop()
                
            deque.append(i)
            
            if i - deque[0] == k:
                deque.popleft()
                
            if  i+1 >= k:
                result.append(nums[deque[0]])
                
        return result                
            