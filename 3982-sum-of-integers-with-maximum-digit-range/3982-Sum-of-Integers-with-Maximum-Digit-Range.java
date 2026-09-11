class Solution {
    public int maxDigitRange(int[] nums) {
        int maxRange = -1;
        int sum = 0;
        
        for (int num : nums) {
            // Find the min and max digit of the current number
            int minDigit = 9;
            int maxDigit = 0;
            int temp = num;
            
            while (temp > 0) {
                int digit = temp % 10;
                if (digit < minDigit) minDigit = digit;
                if (digit > maxDigit) maxDigit = digit;
                temp /= 10;
            }
            
            int currentRange = maxDigit - minDigit;
            
            // Compare with the global maximum range
            if (currentRange > maxRange) {
                maxRange = currentRange;
                sum = num; // Start a new sum for this maximum range
            } else if (currentRange == maxRange) {
                sum += num; // Accumulate numbers with the same maximum range
            }
        }
        
        return sum;
    }
}