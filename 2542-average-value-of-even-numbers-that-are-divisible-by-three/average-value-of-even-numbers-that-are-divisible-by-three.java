class Solution {
    public int averageValue(int[] nums) {
        int sum = 0;
        int count = 0;
        
        for (int num : nums) {
            // A number is even and divisible by 3 if it is divisible by 6
            if (num % 6 == 0) {
                sum += num;
                count++;
            }
        }
        
        // If no matching numbers were found, return 0 to prevent division by zero
        return count == 0 ? 0 : sum / count;
    }
}