# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head:
            return None
        
        
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        
        self.current = head
        
        def buildBST(left, right):
            if left > right:
                return None
    
            mid = (left + right) // 2
            left_child = buildBST(left, mid - 1)
            root = TreeNode(self.current.val)
            root.left = left_child
            self.current = self.current.next
            
            root.right = buildBST(mid + 1, right)
            
            return root
        
        return buildBST(0, length - 1)