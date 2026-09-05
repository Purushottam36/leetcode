class Solution {
    public int getLeastFrequentDigit(int n) {
        // Step 1: Initialize a frequency array for digits 0-9
        int[] digitCount = new int[10];
        
        // Step 2: Extract digits and record their frequencies
        int temp = n;
        while (temp > 0) {
            digitCount[temp % 10]++;
            temp /= 10;
        }
        
        // Step 3: Track the digit with the minimum frequency
        int ans = -1;
        int minFrequency = Integer.MAX_VALUE;
        
        // Iterate from 0 to 9 to naturally prefer the smallest digit in a tie
        for (int digit = 0; digit <= 9; digit++) {
            // Only consider digits that actually appeared in the number
            if (digitCount[digit] > 0 && digitCount[digit] < minFrequency) {
                minFrequency = digitCount[digit];
                ans = digit;
            }
        }
        
        return ans;
    }
}