# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        if root:
            q.append(root)
            level = 0

        else:
            return 0
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None
            level += 1
        return level