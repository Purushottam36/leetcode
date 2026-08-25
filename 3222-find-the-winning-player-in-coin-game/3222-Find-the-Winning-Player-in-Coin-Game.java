public class Solution {
    public String winningPlayer(int x, int y) {
        // Calculate the maximum number of moves that can be made
        int turns = Math.min(x, y / 4);
        
        // Alice wins on odd turns, Bob wins on even turns
        return (turns % 2 == 1) ? "Alice" : "Bob";
    }
}