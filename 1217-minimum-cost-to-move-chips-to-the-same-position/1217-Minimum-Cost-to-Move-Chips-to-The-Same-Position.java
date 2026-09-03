class Solution {
    public int minCostToMoveChips(int[] position) {
        int oddCount = 0;
        int evenCount = 0;
        
        // Count the number of chips at odd and even positions
        for (int pos : position) {
            if (pos % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }
        
        // The minimum cost is moving the smaller group to the larger group
        return Math.min(oddCount, evenCount);
    }
}