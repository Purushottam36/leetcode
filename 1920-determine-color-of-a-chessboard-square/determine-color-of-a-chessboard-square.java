class Solution {
    public boolean squareIsWhite(String coordinates) {
        // Step 1: Extract the column and row characters from the string
        char colChar = coordinates.charAt(0); // e.g., 'a'
        char rowChar = coordinates.charAt(1); // e.g., '1'
        
        // Step 2: Sum their underlying ASCII numeric values
        int asciiSum = colChar + rowChar;
        
        // Step 3: Check if the sum is odd if it's odd, the square is White (true). If even, it's Black (false).
        return asciiSum % 2 != 0;
    }
}