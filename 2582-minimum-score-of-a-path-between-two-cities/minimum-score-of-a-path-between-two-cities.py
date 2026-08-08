class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        parent = list(range(n + 1))
        # Keep track of the minimum road weight in each component
        min_weight = [float('inf')] * (n + 1)
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j, w):
            root_i = find(i)
            root_j = find(j)
            
            # Combine components and update the minimum weight seen for the root
            if root_i != root_j:
                parent[root_i] = root_j
                min_weight[root_j] = min(min_weight[root_j], min_weight[root_i], w)
            else:
                min_weight[root_j] = min(min_weight[root_j], w)

        # Connect all roads
        for u, v, d in roads:
            union(u, v, d)
            
        # The answer is the min weight assigned to the component containing city 1
        return min_weight[find(1)]