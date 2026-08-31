class Solution {
    public int minOperations(int[] nums, int k) {
        int sum = 0;
        
        // Compute the total sum of all elements in the array
        for (int num : nums) {
            sum += num;
        }
        
        // The minimum decrement operations required is exactly the remainder
        return sum % k;
    }
}