# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        deque = collections.deque([root])
        depth = 0
        
        while deque:
            depth += 1
            for _ in range(len(deque)):
                cur_root = deque.popleft()
                if cur_root.left:
                    deque.append(cur_root.left)
                if cur_root.right:
                    deque.append(cur_root.right)
                    
        return depth