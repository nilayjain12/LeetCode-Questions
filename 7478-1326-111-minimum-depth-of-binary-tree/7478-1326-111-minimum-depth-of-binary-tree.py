# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # base condition for none root
        if not root:
            return 0

        # initialize the queue with root node
        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                return depth
            
            # check if left, then append to queue
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))