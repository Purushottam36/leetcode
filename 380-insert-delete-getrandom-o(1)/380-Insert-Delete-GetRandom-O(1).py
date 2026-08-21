import random

class RandomizedSet:

    def __init__(self):
        # Stores the actual elements
        self.num_list = []
        # Maps value -> index in num_list
        self.pos_map = {}

    def insert(self, val: int) -> bool:
        if val in self.pos_map:
            return False
        
        # Add to the end of the list and track its index
        self.pos_map[val] = len(self.num_list)
        self.num_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos_map:
            return False
        
        # Get the index of the element to delete and the last element
        idx_to_remove = self.pos_map[val]
        last_element = self.num_list[-1]
        
        # Move the last element to the position of the element to delete
        self.num_list[idx_to_remove] = last_element
        self.pos_map[last_element] = idx_to_remove
        
        # Remove the last element from both structures
        self.num_list.pop()
        del self.pos_map[val]
        return True

    def getRandom(self) -> int:
        # random.choice picks an element uniformly at random in O(1) time
        return random.choice(self.num_list)