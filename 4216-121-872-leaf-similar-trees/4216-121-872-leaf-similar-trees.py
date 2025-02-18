# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list1, list2 = [], []

        def dfs(root, leaf_list):
            # base case
            if root and not root.left and not root.right:
                leaf_list.append(root.val)
                return
            
            # checking left subtree
            if root.left:
                dfs(root.left, leaf_list)
            
            # check right subtree
            if root.right:
                dfs(root.right, leaf_list)

            return
        
        # running for 1st
        dfs(root1, list1)

        # running for 2nd
        dfs(root2, list2)

        return list1 == list2