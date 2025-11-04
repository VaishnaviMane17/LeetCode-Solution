# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def dfs(node,path,curr_sum):

            if not node:
                return [ ]

            path.append(node.val)
            curr_sum += node.val
        
            if curr_sum == targetSum and not node.left and not node.right:
                ans.append(list(path))
        
            dfs(node.left, path, curr_sum)
            dfs(node.right, path, curr_sum) 

            path.pop()
        

        dfs(root,[ ], 0)
        return ans
        