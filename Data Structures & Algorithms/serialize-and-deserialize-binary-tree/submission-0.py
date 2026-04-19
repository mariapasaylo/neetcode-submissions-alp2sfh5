# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #traverse dfs tree preorder storing values in an array
        #mark null with n
        #return array merged into a string separated by commas
        preord = []
        def dfs(node):
            if not node:
                preord.append("N")
                return 
            preord.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(preord)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #separate string delimited by ,
        #index to go through array
        #construct binary tree using dfs
        #if N return None 
        #otherwise create a tree node and then recursively process left and right
        #return root

        nodes = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if nodes[i] == "N":
                i+= 1
                return None
            node = TreeNode(int(nodes[i]))
            i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

















