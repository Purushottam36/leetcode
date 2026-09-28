class Solution {
    public int maxDepth(String s) {
        int maxDepth = 0;
        int currentDepth = 0;
        
        // Loop through each character in the string
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            
            if (ch == '(') {
                currentDepth++;
                // Update maxDepth if currentDepth exceeds it
                if (currentDepth > maxDepth) {
                    maxDepth = currentDepth;
                }
            } else if (ch == ')') {
                currentDepth--;
            }
        }
        
        return maxDepth;
    }
}