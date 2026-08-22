class Solution {
    public boolean checkDivisibility(int n) {
        // Create a copy of n to extract digits without destroying the original value
        int temp = n;
        int digitSum = 0;
        int digitProduct = 1;
        
        // Loop until all digits are processed
        while (temp > 0) {
            // Get the last digit of the number
            int digit = temp % 10;
            
            // Add the digit to the running sum
            digitSum += digit;
            
            // Multiply the digit to the running product
            digitProduct *= digit;
            
            // Remove the last digit from the number
            temp /= 10;
        }
        
        // Return true if n is perfectly divisible by the sum of its digit sum and product
        return n % (digitSum + digitProduct) == 0;
    }
}