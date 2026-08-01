# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root:
            queue.append(root)
        level = 0
        levels_list = []
        visible = list()
        def addToList(val, level):
            if level >= len(levels_list):
                levels_list.append([])
            levels_list[level].append(val)

        while len(queue)>0:
            for i in range(len(queue)):
                curr = queue.popleft()
                addToList(curr.val, level)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level+=1

        for levels in levels_list:
            visible.append(levels[-1])
        return visible