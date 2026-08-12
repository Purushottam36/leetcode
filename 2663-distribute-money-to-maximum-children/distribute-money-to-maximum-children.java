class Solution {
    public int distMoney(int money, int children) {
        // Step 1: Every child needs at least 1 dollar
        if (money < children) {
            return -1;
        }
        
        // Step 2: Give 1 dollar to each child upfront
        money -= children;
        
        // Step 3: Calculate how many children can get an extra 7 dollars to total 8
        int ans = money / 7;
        int remainder = money % 7;
        
        // Case A: More or equal 8-dollar shares than children available
        if (ans >= children) {
            if (ans == children && remainder == 0) {
                return children;
            }
            return children - 1;
        }
        
        // Case B: One child is left with exactly 4 dollars (1 initial + 3 remainder)
        if (ans == children - 1 && remainder == 3) {
            return ans - 1;
        }
        
        // Case C: Standard distribution
        return ans;
    }
}