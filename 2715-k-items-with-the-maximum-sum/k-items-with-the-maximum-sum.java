class Solution {
    public int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        // Case 1: We can pick all k items from the available 1s
        if (k <= numOnes) {
            return k;
        }
        
        // Case 2: We use all 1s and some or all 0s (0s don't change the sum)
        if (k <= numOnes + numZeros) {
            return numOnes;
        }
        
        // Case 3: We are forced to pick some -1s
        int remaining = k - numOnes - numZeros;
        return numOnes - remaining;
    }
}