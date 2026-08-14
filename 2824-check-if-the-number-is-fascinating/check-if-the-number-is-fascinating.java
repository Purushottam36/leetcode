class Solution {
    public boolean isFascinating(int n) {
        // Concatenate n, 2*n, and 3*n into a single string
        String concatenated = "" + n + (2 * n) + (3 * n);
        
        // A valid fascinating number combination must have exactly 9 digits
        if (concatenated.length() != 9) {
            return false;
        }
        
        // Track the presence of digits 1-9
        boolean[] seen = new boolean[10];
        
        for (int i = 0; i < concatenated.length(); i++) {
            int digit = concatenated.charAt(i) - '0';
            
            // Fascinating numbers cannot contain '0' or duplicate digits
            if (digit == 0 || seen[digit]) {
                return false;
            }
            
            seen[digit] = true;
        }
        
        return true;
    }
}