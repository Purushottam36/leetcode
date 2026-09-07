class Solution {
    public int minMoves(int[] nums) {
        int maxVal = 0;
        int sum = 0;
        int n = nums.length;
        
        // Find the maximum value and the sum of all elements
        for (int num : nums) {
            if (num > maxVal) {
                maxVal = num;
            }
            sum += num;
        }
        
        // Total moves needed to make all elements equal to maxVal
        return (maxVal * n) - sum;
    }
}