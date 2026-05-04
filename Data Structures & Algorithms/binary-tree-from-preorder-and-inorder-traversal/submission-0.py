# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        indexMap = {val: index for index, val in enumerate(inorder)} 

        if not preorder and not preorder:
            return None
        
        root = TreeNode(preorder[0])
        # recursion
        mid = indexMap[root.val]
        leftLength = mid
        root.left = self.buildTree(preorder[1 : leftLength + 1], inorder[: mid])
        root.right = self.buildTree(preorder[leftLength + 1 : ], inorder[mid + 1: ])
        
        
        return root 
