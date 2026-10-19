# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        stack1 = []
        stack2 = []
        
        # Push all digits of l1 onto stack1
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
            
        # Push all digits of l2 onto stack2
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        carry = 0
        head = None
        
        # Process digits from right to left
        while stack1 or stack2 or carry:
            total_sum = carry
            
            if stack1:
                total_sum += stack1.pop()
            if stack2:
                total_sum += stack2.pop()
                
            carry = total_sum // 10
            
            # Create a new node and insert it at the front of the resulting list
            new_node = ListNode(total_sum % 10)
            new_node.next = head
            head = new_node
            
        return head