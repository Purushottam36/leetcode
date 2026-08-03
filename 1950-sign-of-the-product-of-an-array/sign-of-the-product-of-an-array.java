class Solution {
    public int arraySign(int[] nums) {
        // Start with a positive sign representation
        int sign = 1;

        for (int num : nums) {
            // Any zero instantly makes the entire product zero
            if (num == 0) {
                return 0;
            }
            // A negative number flips the current sign
            if (num < 0) {
                sign = -sign;
            }
        }

        return sign;
    }
}