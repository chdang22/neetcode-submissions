# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        values = []
        level = 0
        def addToList(val, level):
            if level >= len(values):
                values.append([])
            values[level].append(val)
        if root:
            queue.append(root)

        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                addToList(curr.val, level)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
        return values
