class Solution {
    public int divisorSubstrings(int num, int k) {
        String numStr = String.valueOf(num);
        int beautyCount = 0;
        
        // Slide a window of size k across the string
        for (int i = 0; i <= numStr.length() - k; i++) {
            String substring = numStr.substring(i, i + k);
            int val = Integer.parseInt(substring);
            
            // Avoid division by zero and check if it's a valid divisor
            if (val != 0 && num % val == 0) {
                beautyCount++;
            }
        }
        
        return beautyCount;
    }
}