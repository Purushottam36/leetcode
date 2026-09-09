class Solution {
    public int mirrorDistance(int n) {
        long original = n;
        long reversed = 0;
        long temp = n;
        
        // Reverse the integer using arithmetic operations
        while (temp > 0) {
            reversed = reversed * 10 + (temp % 10);
            temp /= 10;
        }
        
        // Compute absolute difference and cast back to int
        return (int) Math.abs(original - reversed);
    }
}