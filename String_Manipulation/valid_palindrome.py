# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

# input: s = "A man, a plan, a canal: Panama"
# output: true
# first solution
import collections
import re
from typing import Deque

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True
#second solution(using Slicing)
class Solution2:
    def isPalindrome2(self, s:str) -> bool:
        s = s.lower()
        s = re.sub('^a-z0-9', '', s)

        return s == s[::-1]