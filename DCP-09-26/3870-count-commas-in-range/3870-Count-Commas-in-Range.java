class Solution {
    public int countCommas(int n) {
        // Numbers less than 1000 contain no commas
        if (n < 1000) {
            return 0;
        }
        
        // Every number from 1000 to n (inclusive) contains exactly 1 comma
        return n - 1000 + 1;
    }
}