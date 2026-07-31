# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.smallest = -1
        
        def inOrder(node):
            if not node or self.cnt >= k: return
            inOrder(node.left)
            self.cnt += 1
            if self.cnt == k:
                self.smallest = node.val
                return
            inOrder(node.right)
        
        inOrder(root)
        return self.smallest