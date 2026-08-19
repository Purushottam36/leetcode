class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n = grid.length;
        int totalElements = n * n;
        
        // Frequency array to keep track of numbers from 1 to n^2
        int[] count = new int[totalElements + 1];
        
        // Count frequencies of each number in the grid
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                count[grid[i][j]]++;
            }
        }
        
        int repeated = -1;
        int missing = -1;
        
        // Find the missing (count == 0) and repeated (count == 2) values
        for (int i = 1; i <= totalElements; i++) {
            if (count[i] == 2) {
                repeated = i;
            } else if (count[i] == 0) {
                missing = i;
            }
            
            // Optimization: break early if both values are found
            if (repeated != -1 && missing != -1) {
                break;
            }
        }
        
        return new int[]{repeated, missing};
    }
}