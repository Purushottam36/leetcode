# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the tree is empty, return the new node as the root
        if not root:
            return TreeNode(val)
        
        current = root
        while True:
            if val > current.val:
                # Target belongs to the right subtree
                if current.right is None:
                    current.right = TreeNode(val)
                    break
                current = current.right
            else:
                # Target belongs to the left subtree
                if current.left is None:
                    current.left = TreeNode(val)
                    break
                current = current.left
                
        return root