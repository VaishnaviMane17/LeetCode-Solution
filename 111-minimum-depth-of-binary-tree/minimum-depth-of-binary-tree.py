# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root.left == None and root.right == None:
            return 1

        if root.left and not root.right:
            left = self.minDepth(root.left)
            return 1 + left

        if not root.left and root.right:
            right = self.minDepth(root.right)
            return 1 + right

        if root.left and root.right:
            left = self.minDepth(root.left)       
            right = self.minDepth(root.right)
        return 1 + min(left,right)
        

