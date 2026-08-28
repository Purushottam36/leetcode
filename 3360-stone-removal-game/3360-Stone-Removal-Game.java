class Solution {
    public boolean canAliceWin(int n) {
        int stonesToRemove = 10;
        int turns = 0;
        
        // Continue the game as long as there are enough stones for the current player's turn
        while (n >= stonesToRemove) {
            n -= stonesToRemove;  // Subtract the stones removed in the current turn
            stonesToRemove--;  // Next player removes 1 fewer stone than the current turn
            turns++;
        }
        
        // If the total number of turns is odd, Alice made the last valid move and wins
        // If it is even, Bob made the last valid move or Alice couldn't make the first move
        return turns % 2 != 0;
    }
}