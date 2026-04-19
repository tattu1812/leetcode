class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        s = [root]
        res = 0
        while s:
            n = s.pop()
            if not n.left and not n.right:
                res += n.val
            if n.left:
                n.left.val = n.val * 10 + n.left.val
                s.append(n.left)
            if n.right:
                n.right.val = n.val * 10 + n.right.val
                s.append(n.right)
        return res