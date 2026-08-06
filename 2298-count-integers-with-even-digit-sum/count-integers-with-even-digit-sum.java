class Solution {
    public int countEven(int num) {
        int count = 0;
        
        // Check every integer from 1 to num
        for (int i = 1; i <= num; i++) {
            if (getDigitSum(i) % 2 == 0) {
                count++;
            }
        }
        return count;
    }
    
    // Helper method to extract and sum digits
    private int getDigitSum(int val) {
        int sum = 0;
        while (val > 0) {
            sum += val % 10;
            val /= 10;
        }
        return sum;
    }
}