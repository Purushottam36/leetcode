class Solution {
    public String trafficSignal(int timer) {
        // Rule 1: If timer == 0, the signal is "Green"
        if (timer == 0) {
            return "Green";
        } 
        // Rule 2: If timer == 30, the signal is "Orange"
        else if (timer == 30) {
            return "Orange";
        } 
        // Rule 3: If 30 < timer <= 90, the signal is "Red"
        else if (timer > 30 && timer <= 90) {
            return "Red";
        } 
        // Catch-all: If none of the conditions match, return "Invalid"
        else {
            return "Invalid";
        }
    }
}