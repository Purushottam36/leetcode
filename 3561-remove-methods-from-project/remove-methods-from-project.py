from collections import deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build the adjacency list for the graph
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
            
        # Step 2: Find all suspicious methods using BFS starting from k
        suspicious = [False] * n
        suspicious[k] = True
        queue = deque([k])
        
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if not suspicious[neighbor]:
                    suspicious[neighbor] = True
                    queue.append(neighbor)
                    
        # Step 3: Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                # External invocation found, cannot remove anything
                return list(range(n))
                
        # Step 4: Return all non-suspicious methods
        return [i for i in range(n) if not suspicious[i]]
