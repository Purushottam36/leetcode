public class Solution {
    public boolean isSameAfterReversals(int num) {
        // Handle the edge case where the number is zero.
        if (num == 0) {
            return true;
        }
        
        // Extract the last digit using the remainder operator.
        int lastDigit = num % 10;
        
        // If the last digit is 0, a reversal will lose information.
        // If the last digit is anything from 1 to 9, information is preserved.
        if (lastDigit == 0) {
            return false;
        } else {
            return true;
        }
    }
}