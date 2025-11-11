# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        max = -math.inf
        lvl = 0
        maxlvl = 0

        while queue:
            lvl += 1
            sum = 0
            for _ in range (len(queue)):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)     
                if node.right:
                    queue.append(node.right)
            if max< sum:
                max, maxlvl = sum, lvl
        return maxlvl


            

        