class Solution {
    public String categorizeBox(int length, int width, int height, int mass) {
        // Prevent overflow by casting to long before multiplying
        long volume = (long) length * width * height;
        
        boolean isBulky = length >= 10000 || 
                          width >= 10000 || 
                          height >= 10000 || 
                          volume >= 1000000000;
                          
        boolean isHeavy = mass >= 100;
        
        if (isBulky && isHeavy) {
            return "Both";
        }
        if (!isBulky && !isHeavy) {
            return "Neither";
        }
        return isBulky ? "Bulky" : "Heavy";
    }
}