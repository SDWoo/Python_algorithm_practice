# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Solution 1
class Solution:
    def reverseList(self, head: ListNode)-> ListNode:
        node, prev = head, None
            
        while node:
            next, node.next = node.next, prev
            prev, node = node, next 
                
        return prev
        
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
                
        return list
        
    def toReversedLinkedList(self, result:str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
                
        return node
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        
        print(a)
        print(b)
        
        result = functools.reduce(lambda x,y: 10 * x + y, a, 0)
        return self.toReversedLinkedList(str(result))

# Solution2
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> Listnode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            if l1:
                sum+= l1.val
                l1 = l1.next
            if l2:
                sum+= l2.val
                l2 = l2.next

        carry.val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

        return root.next