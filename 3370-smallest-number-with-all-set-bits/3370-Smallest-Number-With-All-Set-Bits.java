class Solution {
    public int smallestNumber(int n) {
        int x = 1;
        // Shift left until x is greater than or equal to n
        while (x < n) {
            x = (x << 1) | 1;
        }
        return x;
    }
}