class Solution {
    public long minCuttingCost(int n, int m, int k) {
        // Initialize minCost to the maximum possible value to keep track of the minimum cost found
        long minCost = Long.MAX_VALUE;

        // Loop through all possible ways to cut log n into two pieces (len1 and len2)
        for (int i = 1; i < n; i++) {
            int len1 = i;
            int len2 = n - i;
            
            // Check if both pieces of log n and the uncut log m can fit into the trucks (length <= k)
            if (len1 <= k && len2 <= k && m <= k) {
                long cost = (long) len1 * len2;
                minCost = Math.min(minCost, cost);
            }
        }

        // Loop through all possible ways to cut log m into two pieces (len1 and len2)
        for (int i = 1; i < m; i++) {
            int len1 = i;
            int len2 = m - i;
            
            // Check if both pieces of log m and the uncut log n can fit into the trucks (length <= k)
            if (len1 <= k && len2 <= k && n <= k) {
                long cost = (long) len1 * len2;
                minCost = Math.min(minCost, cost);
            }
        }

        // If both original logs already fit without any cuts, the required total cost is 0
        if (n <= k && m <= k) {
            return 0;
        }
        return minCost;
    }
}