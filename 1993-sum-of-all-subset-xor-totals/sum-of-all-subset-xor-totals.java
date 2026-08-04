public class Solution {
    public int subsetXORSum(int[] nums) {
        return dfs(nums, 0, 0);
    }
    
    private int dfs(int[] nums, int index, int currentXOR) {
        // Base case: processed all elements
        if (index == nums.length) {
            return currentXOR;
        }
        
        // Choice 1: Include the current element in the subset
        int include = dfs(nums, index + 1, currentXOR ^ nums[index]);
        
        // Choice 2: Exclude the current element from the subset
        int exclude = dfs(nums, index + 1, currentXOR);
        
        return include + exclude;
    }
}