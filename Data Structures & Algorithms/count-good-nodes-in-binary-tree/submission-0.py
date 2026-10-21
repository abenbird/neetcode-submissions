# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [[root.val - 1, root]]
        count = 0
        while stack:
            maxCur, node = stack.pop(0)
            if maxCur <= node.val:
                count += 1
                maxCur = node.val
            if node.left:
                stack.append([maxCur, node.left])
            if node.right:
                stack.append([maxCur, node.right])
        return count