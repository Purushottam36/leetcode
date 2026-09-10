class Solution {
    public boolean validDigit(int n, int x) {
        String numStr = String.valueOf(n);
        char digitChar = (char) (x + '0'); // Convert target digit to char

        // Rule 2: It must NOT start with digit x
        if (numStr.charAt(0) == digitChar) {
            return false;
        }

        // Rule 1: It must contain at least one occurrence of digit x
        // Since we know it doesn't start with x, look through the remaining positions
        for (int i = 1; i < numStr.length(); i++) {
            if (numStr.charAt(i) == digitChar) {
                return true;
            }
        }

        return false;
    }
}