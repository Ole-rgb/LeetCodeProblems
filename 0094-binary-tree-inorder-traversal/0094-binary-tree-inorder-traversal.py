# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
                            1

                    2               3
                
            4           5                   6

        1. Go left until you cant 1->2->4 and add to list 
        2. 
        '''
        if root == None:
            return []

        solution = []
 
        if root.left:
            #first add the left sublist 
            solution +=self.inorderTraversal(root.left)
        
        #then add current node value
        solution.append(root.val)
        
        if root.right:
            #then add the right sublist 
            solution +=self.inorderTraversal(root.right)
        
        return solution