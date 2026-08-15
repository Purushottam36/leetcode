class Solution {
    public int countBeautifulPairs(int[] nums) {
        int beautifulPairsCount = 0;
        int n = nums.length;
        
        for (int i = 0; i < n; i++) {
            // Extract the first digit of nums[i]
            int firstDigit = nums[i];
            while (firstDigit >= 10) {
                firstDigit /= 10;
            }
            
            for (int j = i + 1; j < n; j++) {
                // Extract the last digit of nums[j]
                int lastDigit = nums[j] % 10;
                
                // Check if they are coprime
                if (gcd(firstDigit, lastDigit) == 1) {
                    beautifulPairsCount++;
                }
            }
        }
        
        return beautifulPairsCount;
    }
    
    // Helper method to calculate Greatest Common Divisor
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}