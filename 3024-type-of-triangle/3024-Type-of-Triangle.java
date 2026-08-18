class Solution {
    public String triangleType(int[] nums) {
        int a = nums[0];
        int b = nums[1];
        int c = nums[2];

        // 1. Mathematical Validation using the Triangle Inequality Theorem
        if ((a + b <= c) || (a + c <= b) || (b + c <= a)) {
            return "none";
        }

        // 2. Classification using logic/set equivalence
        if (a == b && b == c) {
            return "equilateral";
        }
        
        if (a == b || b == c || a == c) {
            return "isosceles";
        }

        return "scalene";
    }
}