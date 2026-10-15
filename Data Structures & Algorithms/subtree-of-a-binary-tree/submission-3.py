# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                isSame = self.isSameTree(node, subRoot)
                if isSame:
                    return True
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False
                
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        stack1 = [[0, p]]
        stack2 = [[0, q]]
        while stack1 or stack2:
            if len(stack1) != len(stack2):
                return False
            node1T, node1 = stack1.pop()
            node2T, node2 = stack2.pop()
            if not node1 or not node2:
                return False
            if node1T != node2T or node1.val != node2.val:
                return False
            if node1.left:
                stack1.append([1, node1.left])
            if node1.right:
                stack1.append([2, node1.right])
            if node2.left:
                stack2.append([1, node2.left])
            if node2.right:
                stack2.append([2, node2.right])  
        return True