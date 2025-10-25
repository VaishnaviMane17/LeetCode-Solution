# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        def dfs(node, curr_max):
            if node is None:
                return
            
            if node.val >= curr_max:
                self.good+=1
            new_max = max(curr_max, node.val)

            dfs(node.left, new_max)
            dfs(node.right, new_max)

            return
        
        dfs(root, root.val)

        return self.good
            
            

            
            

        