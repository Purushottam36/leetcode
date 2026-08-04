public class Solution {
    public String largestOddNumber(String num) {
        // Scan from right to left to find the first odd digit
        for (int i = num.length() - 1; i >= 0; i--) {
            int digit = num.charAt(i) - '0';
            if (digit % 2 != 0) {
                // Return the substring from the beginning up to this odd digit
                return num.substring(0, i + 1);
            }
        }
        // If no odd digit is found, return an empty string
        return "";
    }
}