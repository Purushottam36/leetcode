class Solution {
    public int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        // Step 1: Calculate the total raw hours accumulated 
        int rawTotalHours = arrivalTime + delayedTime;
        
        // Step 2: Declare the variable to store our final 24-hour formatted time
        int finalArrivalTime;
        
        // Step 3: Branch based on whether the time wraps around to a new day
        if (rawTotalHours >= 24) {
            // If hours equal or exceed 24, subtract a full day (24 hours)
            finalArrivalTime = rawTotalHours - 24;
        } else {
            // If hours are less than 24, the time stays exactly as it is
            finalArrivalTime = rawTotalHours;
        }
        
        // Step 4: Return the computed 24-hour format result
        return finalArrivalTime;
    }
}