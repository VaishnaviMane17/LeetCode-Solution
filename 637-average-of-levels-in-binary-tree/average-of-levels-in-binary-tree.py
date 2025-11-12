# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avg = []
        q = deque([root])

        while q:
            lvl_sum = 0
            leng = len(q)
            for _ in range(len(q)):
                node = q.popleft()
                lvl_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            avg.append(lvl_sum/leng)

        return avg
                    


