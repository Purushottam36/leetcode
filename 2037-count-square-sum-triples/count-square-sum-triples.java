public class Solution {
    public int countTriples(int n) {
        int count = 0;
        
        // Iterate through all possible values of a and b
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                int sumSquares = a * a + b * b;
                
                // Calculate the potential value of c
                int c = (int) Math.sqrt(sumSquares);
                
                // Check if c is within the valid range and satisfies the Pythagorean theorem
                if (c <= n && c * c == sumSquares) {
                    count++;
                }
            }
        }
        
        return count;
    }
}