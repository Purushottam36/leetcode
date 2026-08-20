class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        int sum = 0;
        int temp = x;
        
        // Step 1: Extract and sum all digits
        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }
        
        // Step 2: Check if x is divisible by the digit sum
        if (x % sum == 0) {
            return sum;
        }
        
        // Step 3: Return -1 if it is not a Harshad number
        return -1;
    }
}