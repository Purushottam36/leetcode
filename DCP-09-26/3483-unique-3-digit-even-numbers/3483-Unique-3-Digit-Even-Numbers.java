class Solution {
    public int totalNumbers(int[] digits) {
        // Count frequency of each digit using a fixed array
        int[] available = new int[10];
        for (int d : digits) {
            available[d]++;
        }
        
        int totalCount = 0;
        
        // Loop through every valid 3-digit even number
        for (int num = 100; num < 1000; num += 2) {
            int d1 = num / 100;         // Hundreds place
            int d2 = (num / 10) % 10;   // Tens place
            int d3 = num % 10;          // Ones place
            
            // Temporarily consume the digits
            available[d1]--;
            available[d2]--;
            available[d3]--;
            
            // If all counts remain 0 or higher, the number is valid
            if (available[d1] >= 0 && available[d2] >= 0 && available[d3] >= 0) {
                totalCount++;
            }
            
            // Restore the counts for the next check
            available[d1]++;
            available[d2]++;
            available[d3]++;
        }
        
        return totalCount;
    }
}