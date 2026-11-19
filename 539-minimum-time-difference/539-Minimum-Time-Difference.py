class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        # More than 1440 time points guarantees at least one duplicate
        if len(timePoints) > 1440:
            return 0
        
        # Convert "HH:MM" to total minutes past midnight
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            minutes.append(h * 60 + m)
            
        minutes.sort()
        
        # Initialize with the circular wrap-around difference across midnight
        min_diff = (1440 - minutes[-1]) + minutes[0]
        
        # Check all adjacent pairs
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
            
        return min_diff