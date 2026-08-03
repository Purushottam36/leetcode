class Solution {
    public int sumBase(int n, int k) {
        int sum = 0;
        
        while (n > 0) {
            // Extract the last digit in base k
            sum += n % k;
            // Reduce n by a factor of k
            n /= k;
        }
        
        return sum;
    }
}