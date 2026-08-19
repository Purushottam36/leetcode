class Solution {
    public int sumOfEncryptedInt(int[] nums) {
        int totalSum = 0;
        
        for (int num : nums) {
            totalSum += encrypt(num);
        }
        
        return totalSum;
    }
    
    private int encrypt(int x) {
        int maxDigit = 0;
        int count = 0;
        
        // Extract digits mathematically
        while (x > 0) {
            int digit = x % 10;
            if (digit > maxDigit) {
                maxDigit = digit;
            }
            count++;
            x /= 10;
        }
        
        // Generate the matching wall of 1s (e.g., 3 digits -> 111)
        int wallOfOnes = 0;
        while (count > 0) {
            wallOfOnes = wallOfOnes * 10 + 1;
            count--;
        }
        
        // Encrypted value is maxDigit repeated (e.g., 5 * 111 = 555)
        return maxDigit * wallOfOnes;
    }
}