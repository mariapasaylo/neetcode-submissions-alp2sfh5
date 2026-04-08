# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #input: roots of binary tree and subroot
        #output: true subroot exists in subtree of root otherwise falce

        #similar to finding if two trees are the same given the root
        #dfs
        #O(m*n) where m num nodes in root and n num nodes in SubRoot 

        #if subRoot is empty
        #   return True
        #if root is empty
        #   return False

        #if sameTree(root, subRoot)
        #   return True

        #return recursive call to traverse left of root OR right of root

        #helper sameTree(root, subRoot) -this checks if two trees are the same
            #base case
            #left and right not null
            #   return true

            #if root and subroot and root.val == subroot.val 
            #   return traverse left of root and subroot AND traverse right of root and subroot
            #else
            #   return false
        
        if not subRoot:
            return True #because empty tree is always a subtree
        if not root:
            return False #because subRoot would not be a subtree in an empty tree
        
        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode],subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: #both empty
            return True
        if root and subRoot and root.val == subRoot.val: #same structure and values
            #traverse lef tna right of both trees
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        
        return False   


