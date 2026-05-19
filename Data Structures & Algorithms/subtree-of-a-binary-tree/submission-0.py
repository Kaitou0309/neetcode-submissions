# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True 
        
        def helper(p, q): 
            
            nonlocal res 
            
            if not(p or q):
                return 
            
            if (not p and q) or (p and not q) or (p.val != q.val): 
                res = False 
                return
                
            helper(p.left, q.left)
            helper(p.right, q.right)
            
            return 
        
        helper(p, q)
        return res
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root: 
            return False
        
        # helper function only called when root.val == subRoot.val 
        # else continue traverse the tree to find matching val
        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
        