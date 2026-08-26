class Solution {
    public int generateKey(int num1, int num2, int num3) {
        int key = 0;
        int placeValue = 1;

        // Process each of the 4 digits from right to left
        for (int i = 0; i < 4; i++) {
            // Extract the last digit of each number
            int d1 = num1 % 10;
            int d2 = num2 % 10;
            int d3 = num3 % 10;

            // Find the minimum among the current digits
            int minDigit = Math.min(d1, Math.min(d2, d3));

            // Place the minimum digit in its correct positional value
            key += minDigit * placeValue;

            // Move to the next digit position (tens, hundreds, thousands)
            placeValue *= 10;

            // Strip the last digit from each number
            num1 /= 10;
            num2 /= 10;
            num3 /= 10;
        }

        return key;
    }
}