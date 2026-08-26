class Solution {
    // Standard LeetCode method name from the description
    public boolean checkTwoChessboardSquares(String coordinate1, String coordinate2) {
        int sum1 = coordinate1.charAt(0) + coordinate1.charAt(1);
        int sum2 = coordinate2.charAt(0) + coordinate2.charAt(1);
        return (sum1 % 2) == (sum2 % 2);
    }

    // Alias method to resolve the __Driver__.java script mismatch
    public boolean checkTwoChessboards(String coordinate1, String coordinate2) {
        return checkTwoChessboardSquares(coordinate1, coordinate2);
    }
}