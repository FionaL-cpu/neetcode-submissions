# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root: 
            return False

        def isSametree(root1, root2) ->bool: #true 
            if not root1 and not root2: 
                return True
            if not root1 or not root2 or root1.val != root2.val:
                return False
            #recursion 
            return isSametree(root1.left, root2.left) and isSametree(root1.right, root2.right)


        #basic case 
        if isSametree(root,subRoot):
            return True
        # recursion 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
            

