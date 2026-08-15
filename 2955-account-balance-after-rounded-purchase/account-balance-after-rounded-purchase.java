class Solution {
    public int accountBalanceAfterPurchase(int purchaseAmount) {
        // Add 5 to handle rounding up for values ending in 5 or more.
        // Divide by 10 to drop the last digit, then multiply by 10 to get the multiple.
        int roundedAmount = ((purchaseAmount + 5) / 10) * 10;
        
        // Subtract the rounded amount from the starting balance of 100.
        return 100 - roundedAmount;
    }
}