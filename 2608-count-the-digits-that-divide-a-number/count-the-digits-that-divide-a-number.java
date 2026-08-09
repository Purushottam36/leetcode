class Solution {
    public int countDigits(int num) {
        int originalNum = num;
        int count = 0;
        
        // Process each digit from right to left
        while (num > 0) {
            int digit = num % 10; 
            
            // Check if the original number is divisible by this digit
            if (originalNum % digit == 0) {
                count++;
            }
            
            // Remove the last digit
            num /= 10;
        }
        
        return count;
    }
}