class Solution {
    public boolean checkPrimeFrequency(int[] nums) {
        // Since 0 <= nums[i] <= 100, an array of size 101 covers all possible elements
        int[] frequency = new int[101];
        
        // 1. Count the frequency of each element
        for (int num : nums) {
            frequency[num]++;
        }
        
        // 2. Check if any element's frequency is a prime number
        for (int freq : frequency) {
            if (freq > 0 && isPrime(freq)) {
                return true; // Short-circuit as soon as we find a prime frequency
            }
        }
        
        return false;
    }
    
    // Helper function to check if a number is prime
    private boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}