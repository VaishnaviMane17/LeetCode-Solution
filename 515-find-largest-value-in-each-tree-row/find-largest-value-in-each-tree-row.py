# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []

        queue = deque([root])
       

        while queue:
            current_row_size = len(queue)
            max_node = -math.inf

            for _ in range(current_row_size):
                node = queue.popleft()
                max_node = max(max_node,node.val)

                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)

            ans.append(max_node)

        return ans
            

            
                



        