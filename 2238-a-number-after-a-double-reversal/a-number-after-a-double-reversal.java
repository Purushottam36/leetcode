class Solution {
    public boolean isSameAfterReversals(int num) {
        // If num is 0, it stays 0 after reversals. Otherwise, it must not be divisible by 10 (no trailing zeros).
        return num == 0 || num % 10 != 0;
    }
}