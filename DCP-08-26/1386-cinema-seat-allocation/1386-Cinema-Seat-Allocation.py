from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Group reservations by row using a bitmask for seats 2 to 9
        # bit 0 corresponds to seat 2, bit 1 to seat 3, ..., bit 7 to seat 9
        occupied_rows = defaultdict(int)
        
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                occupied_rows[row] |= (1 << (seat - 2))
        
        # Start by assuming every single row can host 2 families maximum
        max_groups = 2 * n
        
        # Bitmask patterns for our 3 valid allocations
        # Left block (seats 2,3,4,5)  -> bits 0,1,2,3 -> binary 00001111 -> decimal 15
        # Right block (seats 6,7,8,9) -> bits 4,5,6,7 -> binary 11110000 -> decimal 240
        # Middle block (seats 4,5,6,7) -> bits 2,3,4,5 -> binary 00111100 -> decimal 60
        
        for row, mask in occupied_rows.items():
            # Remove the default 2 groups assigned to this row
            max_groups -= 2
            
            left_free = (mask & 15) == 0
            right_free = (mask & 240) == 0
            middle_free = (mask & 60) == 0
            
            if left_free and right_free:
                max_groups += 2
            elif left_free or right_free or middle_free:
                max_groups += 1
                
        return max_groups