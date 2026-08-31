class Solution {
    public int maxContainers(int n, int w, int maxWeight) {
        // Calculate the maximum total capacity of the cargo deck
        long maxCapacityOnDeck = (long) n * n;
        
        // Calculate how many containers fit based strictly on weight capacity
        long containersByWeight = maxWeight / w;
        
        // The answer is the smaller value between deck capacity and weight capacity
        return (int) Math.min(maxCapacityOnDeck, containersByWeight);
    }
}