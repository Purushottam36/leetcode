import java.util.Arrays;

class Solution {
    public int splitNum(int num) {
        // Step 1: Count total digits to set up the array size
        int temp = num;
        int count = 0;
        while (temp > 0) {
            count++;
            temp /= 10;
        }
        
        // Step 2: Extract digits mathematically using modulo arithmetic
        int[] digits = new int[count];
        int index = 0;
        while (num > 0) {
            digits[index++] = num % 10;
            num /= 10;
        }
        
        // Step 3: Sort digits in ascending order to prioritize smaller leading digits
        Arrays.sort(digits);
        
        int num1 = 0;
        int num2 = 0;
        
        // Step 4: Alternately distribute digits to form the two minimal numbers
        for (int i = 0; i < count; i++) {
            if (i % 2 == 0) {
                num1 = num1 * 10 + digits[i];
            } else {
                num2 = num2 * 10 + digits[i];
            }
        }
        
        return num1 + num2;
    }
}