class Solution {
    public int alternateDigitSum(int n) {
        String s = Integer.toString(n);
        int totalSum = 0;
        int sign = 1;
        
        for (int i = 0; i < s.length(); i++) {
            int digit = Character.getNumericValue(s.charAt(i));
            totalSum += sign * digit;
            sign *= -1; 
        }
        
        return totalSum;
    }
}