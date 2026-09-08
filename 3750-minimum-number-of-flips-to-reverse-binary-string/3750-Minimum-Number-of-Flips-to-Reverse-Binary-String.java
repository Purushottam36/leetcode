class Solution {
    public int minimumFlips(int n) {
        // Get the binary string representation without leading zeros
        String s = Integer.toBinaryString(n);
        int flips = 0;
        int len = s.length();
        
        // Compare bits from the start and end moving inwards
        for (int i = 0; i < len; i++) {
            // Compare character at index i with its mirrored index from the back
            if (s.charAt(i) != s.charAt(len - 1 - i)) {
                flips++;
            }
        }
        
        return flips;
    }
}