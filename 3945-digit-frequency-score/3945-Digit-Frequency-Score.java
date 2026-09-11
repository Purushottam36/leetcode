class Solution {
    public int digitFrequencyScore(int n) {
        int score = 0;
        
        // Extract and sum up every digit in the number
        while (n > 0) {
            score += n % 10; // Get the last digit
            n /= 10;         // Remove the last digit
        }
        
        return score;
    }
}