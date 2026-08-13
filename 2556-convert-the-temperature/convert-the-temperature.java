class Solution {
    public double[] convertTemperature(double celsius) {
        // Apply the given formulas directly and return the array
        return new double[] {celsius + 273.15, celsius * 1.80 + 32.00};
    }
}