# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return true
        
        return self.__isMirror(root.left,root.right)
    
    def __isMirror(self, left, right)->bool:
        #if both nodes are None, its symmetric
        if left == None and right == None:
            return True
        #if one of the nodes is None, its not symmetric
        if left == None or right == None:
            return False
        # compare the value of the given notes and recursively check the child nodes
        return left.val == right.val and self.__isMirror(left.left, right.right) and self.__isMirror(left.right, right.left) 
