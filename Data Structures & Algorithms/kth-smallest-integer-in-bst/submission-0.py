# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #input: root of tree and kth element
        #output: kth smallest value

        #traverse the tree using dfs
        #this guarantees that it will be in order
        #left root right
        #return kth element of array

        nums = []
        #cnt = 0
        def dfs(root):
            if not root:
                return nums

            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return nums[k-1]