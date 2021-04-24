# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        left = True
        right = True
        
        if not p and not q:
            return True
        elif (not p and q) or (p and not q):
            return False
        elif p.val != q.val:
            return False
        
        if p.left and q.left:
            left = self.isSameTree(p.left, q.left)
        elif p.left != q.left:
            return False
        
        if p.right and q.right:
            right = self.isSameTree(p.right, q.right)
        elif p.right != q.right:
            return False
        
        return left and right
            
