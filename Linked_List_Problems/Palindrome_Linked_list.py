# Given the head of a singly linked list, return true if it is a palindrome.

# Input: head = [1,2,2,1]
# Output: true.

# Solution 1
import collections


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q : Deque = collections.deque()

        if not head:
            return True

        node = head
        while node is None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

# Solution 2
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev