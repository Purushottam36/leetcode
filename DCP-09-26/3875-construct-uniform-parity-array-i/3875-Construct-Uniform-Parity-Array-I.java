class Solution {
    public boolean uniformArray(int[] nums1) {
        int oddCount = 0;
        int evenCount = 0;

        // 1. Count the number of even and odd values in the array
        for (int num : nums1) {
            if (num % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }

        // 2. Can we make them all EVEN?
        // - If all are already even, yes.
        // - If there is at least one odd number, we can change another odd to even (Odd - Odd = Even).
        // - Exception: If there is exactly ONE odd number, we cannot make it even unless there is a second odd number to subtract from it.
        boolean canMakeAllEven = (oddCount == 0) || (oddCount > 1);

        // 3. Can we make them all ODD?
        // - If all are already odd, yes.
        // - If there is at least one odd number, we can turn all evens to odd (Even - Odd = Odd).
        boolean canMakeAllOdd = (evenCount == 0) || (oddCount >= 1);

        // Return true if either strategy works
        return canMakeAllEven || canMakeAllOdd;
    }
}