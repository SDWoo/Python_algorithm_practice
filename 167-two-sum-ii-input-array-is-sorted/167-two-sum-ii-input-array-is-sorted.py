class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while not left == right:
            tar = numbers[left] + numbers[right]
            if tar > target:
                right -= 1
            elif tar < target:
                left += 1
            else:
                return [left+1, right+1]
# Solution 2
class Solution:
    def twoSum(self, numbers: List[int], target:int) -> List[int]:
        for i, n in enumerate(numbers):
            left, right = i+1, len(numbers) -1
            expected = target - n
            while left <= right:
                mid = left + (right-left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return i+1, mid+1

# Solution 3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers[k+1:], expected)
            if i < len(numbers[k+1:]) and numbers[i+k+1] == expected:
                return k+1, i+k+2
# 변형
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k+1)
            if i < len(numbers) and numbers[i] == expected:
                return k+1, i+1