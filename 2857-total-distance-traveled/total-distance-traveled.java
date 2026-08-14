class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        int fuelUsed = 0;
        
        while (mainTank >= 5) {
            // Consume 5 liters
            mainTank -= 5;
            fuelUsed += 5;
            
            // If additional tank has fuel, transfer 1 liter to main tank
            if (additionalTank > 0) {
                additionalTank--;
                mainTank += 1;
            }
        }
        
        // Burn whatever remaining fuel is left in the main tank
        fuelUsed += mainTank;
        
        // Total distance = total fuel used * 10 km/liter
        return fuelUsed * 10;
    }
}