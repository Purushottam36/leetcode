class Solution {
    public int largestInteger(int n, int s) {
        // If s is 0, the largest number is always 0, regardless of n
        if (s == 0) {
            return 0;
        }
        
        // The maximum possible sum with n digits is n * 9
        if (s > n * 9) {
            return -1;
        }
        
        StringBuilder sb = new StringBuilder();
        
        // Greedily place the largest possible digits from left to right
        for (int i = 0; i < n; i++) {
            if (s >= 9) {
                sb.append('9');
                s -= 9;
            } else {
                sb.append(s);
                s = 0;
            }
        }
        
        // Convert the constructed string to an integer
        return Integer.parseInt(sb.toString());
    }
}