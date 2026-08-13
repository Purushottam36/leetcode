class Solution {
    public int numberOfCuts(int n) {
        // A circle with 1 slice requires 0 cuts.
        if (n == 1) {
            return 0;
        }
        // If n is even, each full line cut through the center creates 2 slices.
        // If n is odd, each cut can only go from the edge to the center.
        return (n % 2 == 0) ? n / 2 : n;
    }
}