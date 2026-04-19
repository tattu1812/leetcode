# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def f(self , p , ina , l , r):
        if l > r : return None
        
        val = p[self.i]
        self.i += 1
        root = TreeNode(val)

        it = ina.index(val , l , r + 1)

        root.left = self.f(p , ina , l , it - 1)
        root.right = self.f(p , ina , it + 1 , r)

        return root

    def buildTree(self, preorder, inorder):
        self. i = 0
        return self.f(preorder , inorder , 0 , len(preorder) - 1)