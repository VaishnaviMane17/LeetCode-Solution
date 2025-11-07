# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs_from(node, curr_sum):
            if not node:
                return 0
            curr_sum += node.val
            count = 1 if curr_sum == targetSum else 0
            count += dfs_from(node.left, curr_sum)
            count += dfs_from(node.right, curr_sum)
            return count

        def traverse(node):
            if not node:
                return 0
            # ✅ Call dfs_from to start new path from this node
            return dfs_from(node, 0) + traverse(node.left) + traverse(node.right)

        return traverse(root)

        