class Solution {
    public int findClosest(int x, int y, int z) {
        // Calculate the absolute step distances to Person 3
        int dist1 = Math.abs(x - z);
        int dist2 = Math.abs(y - z);
        
        // Compare distances to determine who arrives first
        if (dist1 < dist2) {
            return 1;
        } else if (dist2 < dist1) {
            return 2;
        } else {
            return 0;
        }
    }
}