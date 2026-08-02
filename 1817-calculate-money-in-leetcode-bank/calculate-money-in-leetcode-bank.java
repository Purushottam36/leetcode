class Solution {
    public int totalMoney(int n) {
        int totalMoney = 0;
        int mondayDeposit = 1;
        
        while (n > 0) {
            // Deposit money for up to 7 days of the current week
            int daysToDeposit = Math.min(n, 7);
            for (int day = 0; day < daysToDeposit; day++) {
                totalMoney += (mondayDeposit + day);
            }
            // Transition to the next week
            n -= 7;
            mondayDeposit++;
        }
        
        return totalMoney;
    }
}