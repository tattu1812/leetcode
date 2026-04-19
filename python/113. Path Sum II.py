
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        ans = []
        def dfs(node, path, cur_sum):
            if not node:
                return
            path.append(node.val)
            cur_sum += node.val

            if sum(path) == targetSum and node.left is None and node.right is None:
                ans.append(path[:])
        
            dfs(node.left, path, cur_sum)
            dfs(node.right, path, cur_sum)

            path.pop()
            

        dfs(root, [], 0)
        
        return ans