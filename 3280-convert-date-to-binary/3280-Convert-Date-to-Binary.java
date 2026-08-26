class Solution {
    public String convertDateToBinary(String date) {
        // Split the date string into ["yyyy", "mm", "dd"]
        String[] parts = date.split("-");
        
        // Convert each part to an integer, then to a binary string
        String yearBin = Integer.toBinaryString(Integer.parseInt(parts[0]));
        String monthBin = Integer.toBinaryString(Integer.parseInt(parts[1]));
        String dayBin = Integer.toBinaryString(Integer.parseInt(parts[2]));
        
        // Join the components back together with hyphens
        return yearBin + "-" + monthBin + "-" + dayBin;
    }
}