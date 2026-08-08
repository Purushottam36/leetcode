class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = [False] * n
        complete_components_count = 0
        
        for i in range(n):
            if not visited[i]:
                component = []
                queue = [i]
                visited[i] = True
                
                head = 0
                while head < len(queue):
                    curr = queue[head]
                    head += 1
                    component.append(curr)
                    for neighbor in graph[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                # Check if every single vertex in this component is connected to all others
                target_degree = len(component) - 1
                if all(len(graph[node]) == target_degree for node in component):
                    complete_components_count += 1
                    
        return complete_components_count