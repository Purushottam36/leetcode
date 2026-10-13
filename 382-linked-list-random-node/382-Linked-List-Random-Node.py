import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def __init__(self, head: ListNode | None):
        """
        Initializes the object with the head of the singly-linked list.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Chooses a node randomly from the list and returns its value.
        Each node has an equal probability of being chosen.
        """
        curr = self.head
        chosen_value = curr.val  # Default to the first node's value
        i = 1
        
        while curr:
            # Pick a random number between 1 and i inclusive.
            # The probability of picking 1 is exactly 1/i.
            if random.randint(1, i) == 1:
                chosen_value = curr.val
            
            # Advance to the next node and increment index
            curr = curr.next
            i += 1
            
        return chosen_value


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()