class Solution {
    public int maximumLengthSubstring(String s) {
        // Array to count frequencies of characters ('a' through 'z')
        int[] charCount = new int[26];
        int maxLen = 0;
        int left = 0;
        
        // Expand the window using the right pointer
        for (int right = 0; right < s.length(); right++) {
            int rightCharIndex = s.charAt(right) - 'a';
            charCount[rightCharIndex]++;
            
            // If any character exceeds 2 occurrences, shrink the window from the left
            while (charCount[rightCharIndex] > 2) {
                int leftCharIndex = s.charAt(left) - 'a';
                charCount[leftCharIndex]--;
                left++;
            }
            
            // Update the maximum length found so far
            maxLen = Math.max(maxLen, right - left + 1);
        }
        
        return maxLen;
    }
}