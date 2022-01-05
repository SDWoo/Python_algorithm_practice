# Write a function that reverses a string. The input string is given as an array of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra memory.
#
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Solution 1
class Solution1:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left +=1
            right -=1
# solution 2
class Solution2:
    def reverseString2(self, s:List(str)) -> None:
        s.reverse()