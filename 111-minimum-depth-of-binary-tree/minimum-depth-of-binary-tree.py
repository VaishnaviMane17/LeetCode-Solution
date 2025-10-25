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

        left = self.minDepth(root.left)       
        right = self.minDepth(root.right)

        if right == 0 :
            return 1 + left

        if left == 0 :
            return 1 + right
            
        return 1 + min(left,right)
        

