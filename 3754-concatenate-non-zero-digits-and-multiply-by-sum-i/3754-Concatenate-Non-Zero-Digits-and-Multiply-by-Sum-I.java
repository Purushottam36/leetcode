class Solution {
    public long sumAndMultiply(int n) {
        // Handle edge case for 0
        if (n == 0) {
            return 0;
        }

        long x = 0;
        long sum = 0;
        
        // Convert to string to process digits from left to right
        String s = Integer.toString(n);
        
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch != '0') {
                int digit = ch - '0';
                x = x * 10 + digit; // Append digit to x
                sum += digit;       // Add digit to total sum
            }
        }
        
        return x * sum;
    }
}