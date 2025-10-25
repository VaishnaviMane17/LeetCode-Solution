# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def max_diff(root, curr_min, curr_max):
            if not root:
                return curr_max - curr_min

            curr_min = min(curr_min, root.val)
            curr_max = max(curr_max, root.val)

            left = max_diff(root.left, curr_min, curr_max)
            right = max_diff(root.right, curr_min, curr_max)
            
            return max(left,right)

        return max_diff(root, root.val, root.val)