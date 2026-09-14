class Solution {
    public boolean canReach(int[] start, int[] target) {
        // Calculate the color parity of both squares
        int startParity = (start[0] + start[1]) % 2;
        int targetParity = (target[0] + target[1]) % 2;
        
        // A knight can only reach the target in an even number of moves 
        // if both squares are the same color (have matching parity)
        return startParity == targetParity;
    }
}