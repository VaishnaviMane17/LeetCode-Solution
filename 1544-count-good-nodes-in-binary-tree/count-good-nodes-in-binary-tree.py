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

        stack = [(root, root.val)]
        ans = 0
        while stack:
            node, max_so_far = stack.pop()
            if node.val >= max_so_far:
                ans += 1

        
            if node.left:
                left = (node.left, max(node.val, max_so_far))
                stack.append(left)
            if node.right:
                right = (node.right, max(node.val, max_so_far))
                stack.append(right)
        
        return ans
            
            

            
            

        