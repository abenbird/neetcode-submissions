# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [root]
        mps = {None: 0}
        while stack:
            node = stack[-1]
            if node.left and node.left not in mps:
                stack.append(node.left)
            elif node.right and node.right not in mps:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftH = mps[node.left]
                rightH = mps[node.right]
                if abs(leftH - rightH) > 1:
                    return False
                mps[node] = 1 + max(leftH, rightH)
        return True
            