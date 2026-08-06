class Solution {
    public int smallestNumber(int n, int t) {
        while (true) {
            int digitProduct = 1;
            int temp = n;
            
            // Extract digits and calculate their product
            while (temp > 0) {
                digitProduct *= (temp % 10);
                temp /= 10;
            }
            
            // Check if the product is divisible by t
            if (digitProduct % t == 0) {
                return n;
            }
            
            // Try the next number
            n++;
        }
    }
}