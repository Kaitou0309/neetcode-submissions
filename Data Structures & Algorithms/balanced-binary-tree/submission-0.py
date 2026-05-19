# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        
        # count depth from the node (subtree) called on 
        def count_depth(root): 
            nonlocal res
            if root == None: 
                return 0
            
            l_depth = count_depth(root.left)
            r_depth = count_depth(root.right)
                        
            if abs(l_depth - r_depth) > 1: 
                res = False
            
            return 1 + max(l_depth, r_depth)
            
        count_depth(root)
        return res 
    