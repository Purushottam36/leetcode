import java.util.Arrays;

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        
        // Sort the array lexicographically
        Arrays.sort(strs);
        
        String first = strs[0];
        String last = strs[strs.length - 1];
        int i = 0;
        
        // Compare the first and last strings character by character
        while (i < first.length() && i < last.length()) {
            if (first.charAt(i) != last.charAt(i)) {
                break;
            }
            i++;
        }
        
        return first.substring(0, i);
    }
}