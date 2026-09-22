from typing import List

class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        # Each node stores: [total_product_mod_k, [frequencies_of_remainders]]
        self.tree_prod = [1] * (4 * self.n)
        self.tree_remain = [[0] * k for _ in range(4 * self.n)]
        self.build(nums, 1, 0, self.n - 1)

    def merge(self, left_node: int, right_node: int, dest_node: int):
        # Calculate combined total product
        left_prod = self.tree_prod[left_node]
        right_prod = self.tree_prod[right_node]
        self.tree_prod[dest_node] = (left_prod * right_prod) % self.k
        
        # Merge prefix remainder frequencies
        dest_remain = [0] * self.k
        left_remain = self.tree_remain[left_node]
        right_remain = self.tree_remain[right_node]
        
        for i in range(self.k):
            # Left counts carry over exactly
            dest_remain[i] += left_remain[i]
            # Right counts are multiplied/shifted by the left product mod k
            new_rem = (i * left_prod) % self.k
            dest_remain[new_rem] += right_remain[i]
            
        self.tree_remain[dest_node] = dest_remain

    def build(self, nums: List[int], node: int, start: int, end: int):
        if start == end:
            val_mod = nums[start] % self.k
            self.tree_prod[node] = val_mod
            self.tree_remain[node][val_mod] = 1
            return
            
        mid = (start + end) // 2
        self.build(nums, 2 * node, start, mid)
        self.build(nums, 2 * node + 1, mid + 1, end)
        self.merge(2 * node, 2 * node + 1, node)

    def update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            val_mod = val % self.k
            self.tree_prod[node] = val_mod
            self.tree_remain[node] = [0] * self.k
            self.tree_remain[node][val_mod] = 1
            return
            
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.merge(2 * node, 2 * node + 1, node)

    def query(self, node: int, start: int, end: int, l: int, r: int):
        if l <= start and end <= r:
            return self.tree_prod[node], self.tree_remain[node]
            
        mid = (start + end) // 2
        if r <= mid:
            return self.query(2 * node, start, mid, l, r)
        if l > mid:
            return self.query(2 * node + 1, mid + 1, end, l, r)
            
        # If the range spans across both children, fetch and merge their results manually
        left_prod, left_remain = self.query(2 * node, start, mid, l, r)
        right_prod, right_remain = self.query(2 * node + 1, mid + 1, end, l, r)
        
        merged_prod = (left_prod * right_prod) % self.k
        merged_remain = [0] * self.k
        for i in range(self.k):
            merged_remain[i] += left_remain[i]
            new_rem = (i * left_prod) % self.k
            merged_remain[new_rem] += right_remain[i]
            
        return merged_prod, merged_remain


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        st = SegmentTree(nums, k)
        result = []
        
        for index_i, value_i, start_i, x_i in queries:
            # Step 1: Persistently update the element
            st.update(1, 0, st.n - 1, index_i, value_i)
            
            # Step 2: Query the range from start_i to the end of the array
            _, remain_freq = st.query(1, 0, st.n - 1, start_i, st.n - 1)
            
            # Step 3: Append the count of prefixes producing remainder x_i
            result.append(remain_freq[x_i])
            
        return result