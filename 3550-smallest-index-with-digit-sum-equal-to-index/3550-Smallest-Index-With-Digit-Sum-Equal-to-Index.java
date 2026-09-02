class Solution {
    public int smallestIndex(int[] nums) {
        // Iterate through the array sequentially to find the smallest index first
        for (int i = 0; i < nums.length; i++) {
            if (getDigitSum(nums[i]) == i) {
                return i;
            }
        }
        // Return -1 if no matching index is found
        return -1;
    }

    // Helper method to calculate the sum of digits of a number
    private int getDigitSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}