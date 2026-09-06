class Solution {
    public long removeZeros(long n) {
        long result = 0;
        long multiplier = 1;
        
        while (n > 0) {
            long digit = n % 10;
            if (digit != 0) {
                result = digit * multiplier + result;
                multiplier *= 10;
            }
            n /= 10;
        }
        
        return result;
    }
}