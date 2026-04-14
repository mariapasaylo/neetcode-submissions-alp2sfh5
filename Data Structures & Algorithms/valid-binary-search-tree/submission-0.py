# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #input root 
        #output true if valid bst otherwise false

        #bst if left < right
        #traverse tree dfs
        #use an interval to define lower and upper limits
        #check max of left tree and min of right

        #helper function(node, left, right)
            #base case
            #if the node exists
            #   return True
            #if the node val is NOT less greater than left and less than right
            #   return false
            #traverse left where min is left and max is curr node AND right where min curr node and max is right

        #call helper function starting at -inf and +inf
        def valid(node, left, right):
            if not node:
                return True
            if not(left < node.val < right):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float("-inf"), float("inf") )



