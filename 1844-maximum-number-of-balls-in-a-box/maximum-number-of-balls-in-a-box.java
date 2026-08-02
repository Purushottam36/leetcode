class Solution {
    public int countBalls(int lowLimit, int highLimit) {
        int[] boxCounts = new int[46];
        int maxBalls = 0;
        
        for (int ball = lowLimit; ball <= highLimit; ball++) {
            int digitSum = 0;
            int temp = ball;
            while (temp > 0) {
                digitSum += temp % 10;
                temp /= 10;
            }
            boxCounts[digitSum]++;
            maxBalls = Math.max(maxBalls, boxCounts[digitSum]);
        }
        
        return maxBalls;
    }
}