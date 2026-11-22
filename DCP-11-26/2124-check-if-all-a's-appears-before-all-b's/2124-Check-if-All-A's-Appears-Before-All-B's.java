class Solution {
    public boolean checkString(String s) {
        boolean seenB = false;
        
        for (char c : s.toCharArray()) {
            if (c == 'b') {
                seenB = true;
            } else if (seenB) { // c is 'a' after a 'b' was already seen
                return false;
            }
        }
        
        return true;
    }
}