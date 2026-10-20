# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [[0, root]]
        res = []
        while stack:
            level, node = stack.pop(0)
            nextLevel = level + 1
            if len(res) < nextLevel:
                res.append(node.val)
                
            if node.right:
                stack.append([nextLevel, node.right])
            if node.left:
                stack.append([nextLevel, node.left])
        return res
