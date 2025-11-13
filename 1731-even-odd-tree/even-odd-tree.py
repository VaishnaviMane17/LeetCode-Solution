# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        q = deque([root])
        lvl = 0

        while q:
            if lvl%2 == 0:
                prev = float('-inf')
            else:
                prev = float('inf')

            for _ in range (len(q)):
                node = q.popleft()
                if lvl%2 == 0 and node.val%2 != 0 and prev < node.val:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                elif lvl%2 != 0 and node.val%2 == 0 and prev > node.val:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    return False
                prev = node.val
            lvl += 1
        
        return True
                

        