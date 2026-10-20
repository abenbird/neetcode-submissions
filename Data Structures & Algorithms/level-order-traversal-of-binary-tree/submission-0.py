# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [[0, root]]
        res = []
        while stack:
            level, node = stack.pop(0)
            if level < len(res):
                res[level].append(node.val)
            else:
                res.append([node.val])
            nextLevel = level + 1
            if node.left:
                stack.append([nextLevel, node.left])
            if node.right:
                stack.append([nextLevel, node.right])
        return res