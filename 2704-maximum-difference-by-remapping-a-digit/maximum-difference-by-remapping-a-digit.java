class Solution {
    public int minMaxDifference(int num) {
        String s = Integer.toString(num);
        
        // Step 1: Find the maximum value
        char targetMax = '9';
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != '9') {
                targetMax = s.charAt(i);
                break;
            }
        }
        String maxStr = s.replace(targetMax, '9');
        int maxVal = Integer.parseInt(maxStr);
        
        // Step 2: Find the minimum value
        char targetMin = s.charAt(0);
        String minStr = s.replace(targetMin, '0');
        int minVal = Integer.parseInt(minStr);
        
        // Step 3: Return the difference
        return maxVal - minVal;
    }
}