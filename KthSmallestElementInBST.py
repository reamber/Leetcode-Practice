# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        orderedArr = self.inOrder(root)
        
        return orderedArr[k-1]
        
        
    def inOrder(self, root):
        ans = []
        if root.left:
            ans.extend(self.inOrder(root.left))
        if root:
            ans.append(root.val)
        if root.right:
            ans.extend(self.inOrder(root.right))
            
        return ans
