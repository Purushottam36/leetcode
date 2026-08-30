class Solution {
    public boolean hasSameDigits(String s) {
        // Convert string to character array for fast manipulation
        char[] digits = s.toCharArray();
        int n = digits.length;
        
        // Loop until the length reduces to 2
        while (n > 2) {
            // In-place update to save memory
            for (int i = 0; i < n - 1; i++) {
                int sum = (digits[i] - '0') + (digits[i + 1] - '0');
                digits[i] = (char) ((sum % 10) + '0');
            }
            // The size of the valid string reduces by 1 in each round
            n--;
        }
        
        // Check if the final two digits are equal
        return digits[0] == digits[1];
    }
}