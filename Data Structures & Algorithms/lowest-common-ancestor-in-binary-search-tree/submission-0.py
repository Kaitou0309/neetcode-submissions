# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    

        # traverse until first split, then return that as LCA
        while root: 
            # if both greater, go left
            if root.val > p.val and root.val > q.val:
                root = root.left
            # if both less, go right
            elif root.val < p.val and root.val < q.val:
                root = root.right

            # a spit occur, return result
            else: 
                return root


        
            


        
        