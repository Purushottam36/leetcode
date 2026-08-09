class Solution {
    public int differenceOfSum(int[] nums) {
        int elementSum = 0;
        int digitSum = 0;
        
        for (int num : nums) {
            elementSum += num;
            
            // Extract digits of the current number
            int temp = num;
            while (temp > 0) {
                digitSum += temp % 10;
                temp /= 10;
            }
        }
        
        return elementSum - digitSum;
    }
}