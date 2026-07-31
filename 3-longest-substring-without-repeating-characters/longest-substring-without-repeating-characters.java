import java.util.HashMap;
import java.util.Map;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Map to store characters and their most recent index position in the string.
        Map<Character, Integer> seen = new HashMap<>();
        
        int left = 0;   // The left boundary of our sliding window
        int maxLen = 0; // Tracks the maximum length of a valid substring found so far
        
        // The 'right' pointer expands our sliding window character by character
        for (int right = 0; right < s.length(); right++) {
            char current = s.charAt(right);
            
            // Condition Check: If the current character has already been encountered AND its last recorded index falls inside our active sliding window boundary...
            if (seen.containsKey(current) && seen.get(current) >= left) {
                // We have found a duplicate. Shrink the window by jumping the left pointer directly to the index right after the previous occurrence.
                left = seen.get(current) + 1;
            }
            
            // Record or overwrite the character's position with its newest index
            seen.put(current, right);
            
            // Calculate the size of the current valid window (right - left + 1) and update our maxLen tracker if this window is larger.
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}