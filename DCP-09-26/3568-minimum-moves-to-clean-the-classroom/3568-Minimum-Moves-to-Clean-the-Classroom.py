import collections

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        
        start_r, start_c = -1, -1
        litters = []
        
        # 1. Map locations of 'S' and all 'L' targets
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litters.append((r, c))
                    
        num_litters = len(litters)
        litter_map = {pos: i for i, pos in enumerate(litters)}
        target_mask = (1 << num_litters) - 1
        
        # Determine initial mask state if 'S' sits on litter
        initial_mask = 0
        if (start_r, start_c) in litter_map:
            initial_mask |= (1 << litter_map[(start_r, start_c)])
            
        if initial_mask == target_mask:
            return 0
            
        # 2. Track maximum remaining energy for each state representation
        # Shape: [m][n][1 << num_litters] initialized to -1
        max_energy = [[[-1] * (1 << num_litters) for _ in range(n)] for _ in range(m)]
        
        # Queue format stores: (row, col, current_energy, collected_mask)
        queue = collections.deque([(start_r, start_c, energy, initial_mask)])
        max_energy[start_r][start_c][initial_mask] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        moves = 0
        
        # 3. Layer-by-layer BFS traversal 
        while queue:
            for _ in range(len(queue)):
                r, c, curr_energy, mask = queue.popleft()
                
                # First time we see target_mask via step-by-step BFS is guaranteed shortest
                if mask == target_mask:
                    return moves
                    
                # Prune path if a better or equal energy state reached this configuration already
                if curr_energy < max_energy[r][c][mask]:
                    continue
                    
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Boundary validation and obstacle avoidance
                    if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                        next_energy = curr_energy - 1
                        
                        if next_energy < 0:
                            continue
                            
                        next_mask = mask
                        cell_type = classroom[nr][nc]
                        
                        # Process cell characteristics
                        if cell_type == 'R':
                            next_energy = energy
                        elif cell_type == 'L':
                            litter_idx = litter_map[(nr, nc)]
                            next_mask |= (1 << litter_idx)
                            
                        # Only proceed if we found a path with higher remaining energy
                        if next_energy > max_energy[nr][nc][next_mask]:
                            max_energy[nr][nc][next_mask] = next_energy
                            queue.append((nr, nc, next_energy, next_mask))
                            
            moves += 1
            
        return -1