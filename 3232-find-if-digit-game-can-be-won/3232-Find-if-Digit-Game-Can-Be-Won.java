public class Solution {
    public boolean canAliceWin(int[] nums) {
        int singleDigitSum = 0;
        int doubleDigitSum = 0;
        
        // Separate and accumulate the sums based on digit count
        for (int num : nums) {
            if (num < 10) {
                singleDigitSum += num;
            } else {
                doubleDigitSum += num;
            }
        }
        
        // Alice wins if either group is strictly greater than the other
        return singleDigitSum != doubleDigitSum;
    }
}