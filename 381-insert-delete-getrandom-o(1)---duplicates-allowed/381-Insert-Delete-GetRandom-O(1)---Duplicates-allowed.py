import random

class RandomizedCollection:

    def __init__(self):
        # Stores all elements (including duplicates)
        self.num_list = []
        # Maps value -> set of indices where this value resides in num_list
        self.pos_map = {}

    def insert(self, val: int) -> bool:
        if val not in self.pos_map:
            self.pos_map[val] = set()
            
        not_present = len(self.pos_map[val]) == 0
        self.pos_map[val].add(len(self.num_list))
        self.num_list.append(val)
        return not_present

    def remove(self, val: int) -> bool:
        if val not in self.pos_map or not self.pos_map[val]:
            return False
        
        # 1. Get any existing index of the value to remove
        idx_to_remove = next(iter(self.pos_map[val]))
        last_idx = len(self.num_list) - 1
        last_element = self.num_list[-1]
        
        # 2. Always remove this index from the value's index tracking set
        self.pos_map[val].remove(idx_to_remove)
        
        # 3. Only swap if the element to remove is NOT already the last element
        if idx_to_remove != last_idx:
            # Overwrite the element at idx_to_remove with the last element
            self.num_list[idx_to_remove] = last_element
            # Link the last element to its new position and delete its old position
            self.pos_map[last_element].add(idx_to_remove)
            self.pos_map[last_element].remove(last_idx)
            
        # 4. Remove the element from the list
        self.num_list.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.num_list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()