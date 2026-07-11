# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        allpaths = []
        currpathstack = []
        self.dfs(root, allpaths, currpathstack)
        return allpaths
    
    def dfs(self, node, allpaths, currpathstack):
        currpathstack.append(node.val)
        if node.left is None and node.right is None:
            currpathstr = "->".join([str(x) for x in currpathstack])
            allpaths.append(currpathstr)

        if node.left is not None:
            self.dfs(node.left, allpaths, currpathstack)
        
        if node.right is not None:
            self.dfs(node.right, allpaths, currpathstack)
        
        currpathstack.pop()
