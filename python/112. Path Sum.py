# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):

        def checkSum (node, targetSum, total):
            if not node:
                return False

            total += node.val    

            if not node.left and not node.right:
                 return targetSum == total
                    

            return checkSum(node.left, targetSum, total)  or checkSum(node.right, targetSum, total)
                  

        return checkSum(root,targetSum, 0)