class Node:
    __slots__ = ['max_len', 'pref_len', 'suff_len', 'size']
    def __init__(self, max_len=1, pref_len=1, suff_len=1, size=1):
        self.max_len = max_len
        self.pref_len = pref_len
        self.suff_len = suff_len
        self.size = size

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s_list = list(s)  # Convert to mutable list for easy updates
        tree = [None] * (4 * n)

        def merge(parent_idx: int, left: Node, right: Node, mid_idx: int):
            # Base initialization from left and right children
            p_max = max(left.max_len, right.max_len)
            p_pref = left.pref_len
            p_suff = right.suff_len
            p_size = left.size + right.size

            # Check if characters at the boundary match and can merge
            if s_list[mid_idx] == s_list[mid_idx + 1]:
                combined = left.suff_len + right.pref_len
                if combined > p_max:
                    p_max = combined
                
                # Update prefix length if the entire left side is uniform
                if left.pref_len == left.size:
                    p_pref = left.size + right.pref_len
                
                # Update suffix length if the entire right side is uniform
                if right.suff_len == right.size:
                    p_suff = right.size + left.suff_len

            if tree[parent_idx] is None:
                tree[parent_idx] = Node(p_max, p_pref, p_suff, p_size)
            else:
                p = tree[parent_idx]
                p.max_len = p_max
                p.pref_len = p_pref
                p.suff_len = p_suff
                p.size = p_size

        def build(node: int, start: int, end: int):
            if start == end:
                tree[node] = Node(1, 1, 1, 1)
                return
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            build(left_node, start, mid)
            build(right_node, mid + 1, end)
            merge(node, tree[left_node], tree[right_node], mid)

        def update(node: int, start: int, end: int, idx: int):
            if start == end:
                return
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            if idx <= mid:
                update(left_node, start, mid, idx)
            else:
                update(right_node, mid + 1, end, idx)
            merge(node, tree[left_node], tree[right_node], mid)

        # Build initial segment tree
        build(0, 0, n - 1)
        
        ans = []
        for ch, idx in zip(queryCharacters, queryIndices):
            s_list[idx] = ch
            update(0, 0, n - 1, idx)
            ans.append(tree[0].max_len)
            
        return ans