# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = root.val 

        def dfs(node):
            nonlocal res 

            if not node: 
                return 0 

            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            curr_path_sum = node.val + left_gain + right_gain 

            res = max(res, curr_path_sum) 

            return node.val + max(left_gain, right_gain)

        dfs(root)

        return res