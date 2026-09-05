class Solution {
    public String concatHex36(int n) {
        // Step 1: Calculate n^2 and n^3
        int n2 = n * n;
        int n3 = n * n * n;
        
        // Step 2: Convert n^2 to base-16 (hexadecimal) and capitalize
        String hex = Integer.toString(n2, 16).toUpperCase();
        
        // Step 3: Convert n^3 to base-36 (hexatrigesimal) and capitalize
        String hexatrigesimal = Integer.toString(n3, 36).toUpperCase();
        
        // Step 4: Return the concatenated result
        return hex + hexatrigesimal;
    }
}