# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> list[int]:
        # Track indices of the first and most recent critical points found
        first_cp_idx = -1
        prev_cp_idx = -1
        
        # Track minimum distance found between adjacent critical points
        min_dist = float('inf')
        
        # Pointers to traverse the list
        prev = head
        curr = head.next
        curr_idx = 1  # 0-indexed position tracker
        
        while curr and curr.next:
            nxt = curr.next
            
            # Check if current node is a local maxima or local minima
            is_maxima = curr.val > prev.val and curr.val > nxt.val
            is_minima = curr.val < prev.val and curr.val < nxt.val
            
            if is_maxima or is_minima:
                if first_cp_idx == -1:
                    # Found the very first critical point
                    first_cp_idx = curr_idx
                else:
                    # Update minimum distance with the gap from the previous critical point
                    min_dist = min(min_dist, curr_idx - prev_cp_idx)
                
                # Update the last seen critical point index
                prev_cp_idx = curr_idx
            
            # Move pointers forward
            prev = curr
            curr = nxt
            curr_idx += 1
            
        # If fewer than two critical points were found, return [-1, -1]
        if first_cp_idx == prev_cp_idx:
            return [-1, -1]
            
        # Maximum distance is always the distance between the first and last critical point
        max_dist = prev_cp_idx - first_cp_idx
        
        return [min_dist, max_dist]