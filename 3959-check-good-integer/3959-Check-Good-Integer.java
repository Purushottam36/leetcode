class Solution {
    public boolean checkGoodInteger(int n) {
        int digitSum = 0;
        int squareSum = 0;
        
        // Extract each digit one by one
        while (n > 0) {
            int digit = n % 10;
            
            digitSum += digit;
            squareSum += (digit * digit);
            
            n /= 10; // Remove the processed digit
        }
        
        // A number is good if squareSum - digitSum is at least 50
        return (squareSum - digitSum) >= 50;
    }
}