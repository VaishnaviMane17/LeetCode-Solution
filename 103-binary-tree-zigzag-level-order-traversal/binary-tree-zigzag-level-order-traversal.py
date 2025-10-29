# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = [ ]

        queue = deque([root])
        round = 0

        while queue:
            curr_size = len(queue)
            level = [ ]

            for i in range (curr_size):
                node = queue.popleft()
                if round % 2 == 0:
                    level.append(node.val)
                else:
                    level.insert(0,node.val) 

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            ans.append(level)
            round += 1

        return ans


