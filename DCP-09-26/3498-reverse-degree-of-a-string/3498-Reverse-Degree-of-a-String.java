class Solution {
    public int reverseDegree(String s) {
        int totalDegree = 0;
        
        for (int i = 0; i < s.length(); i++) {
            // 1-indexed position in the string
            int stringPos = i + 1;
            
            // Position in reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1)
            int revAlphabetPos = 'z' - s.charAt(i) + 1;
            
            // Add the product to the total sum
            totalDegree += stringPos * revAlphabetPos;
        }
        
        return totalDegree;
    }
}