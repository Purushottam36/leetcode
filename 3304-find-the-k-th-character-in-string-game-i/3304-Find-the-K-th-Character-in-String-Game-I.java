class Solution {
    public char kthCharacter(int k) {
        StringBuilder word = new StringBuilder("a");
        
        // Keep doubling the string until it is long enough
        while (word.length() < k) {
            int currentLength = word.length();
            for (int i = 0; i < currentLength; i++) {
                // Get the next character in the alphabet
                char nextChar = (char) (word.charAt(i) + 1);
                word.append(nextChar);
            }
        }
        
        // Return the 1-indexed kth character
        return word.charAt(k - 1);
    }
}