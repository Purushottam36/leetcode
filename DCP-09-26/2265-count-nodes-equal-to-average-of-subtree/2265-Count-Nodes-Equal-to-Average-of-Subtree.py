# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.matching_nodes_count = 0
        
        def dfs(node):
            if not node:
                # Return (subtree_sum, subtree_count)
                return 0, 0
            
            # Post-order traversal: Get data from left and right children first
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            # Calculate total sum and count for the current subtree
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            # Check if the integer division matches the node's value
            if current_sum // current_count == node.val:
                self.matching_nodes_count += 1
                
            return current_sum, current_count

        dfs(root)
        return self.matching_nodes_count