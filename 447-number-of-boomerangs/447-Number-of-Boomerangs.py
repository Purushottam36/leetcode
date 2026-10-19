class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        boomerangs = 0
        
        # Iterate through each point, treating it as the pivot 'i'
        for i in range(len(points)):
            # Hash map to store distance -> count of points at this distance from points[i]
            dist_map = {}
            x1, y1 = points[i]
            
            for j in range(len(points)):
                if i == j:
                    continue
                
                x2, y2 = points[j]
                # Calculate squared Euclidean distance to avoid floats
                dx = x1 - x2
                dy = y1 - y2
                d_squared = dx * dx + dy * dy
                
                # Update the count for this distance
                dist_map[d_squared] = dist_map.get(d_squared, 0) + 1
            
            # For each distance group, add count * (count - 1) to total boomerangs
            for count in dist_map.values():
                boomerangs += count * (count - 1)
                
        return boomerangs