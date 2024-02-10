# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Dynamic Programming
        Basecase there are no leafs to explore in current state->return 0
        '''
        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        left=0
        right=0

        # explore child states
        if root.left:
            left += self.maxDepth(root.left)+1

        if root.right:
            right += self.maxDepth(root.right)+1
        
        return max(left, right)