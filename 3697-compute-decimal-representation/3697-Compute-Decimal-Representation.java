import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] decimalRepresentation(int n) {
        List<Integer> components = new ArrayList<>();
        int placeValue = 1;
        
        // Extract digits and their base-10 components from right to left
        while (n > 0) {
            int digit = n % 10;
            if (digit > 0) {
                components.add(digit * placeValue);
            }
            n /= 10;
            placeValue *= 10;
        }
        
        // Convert to the required int[] array in descending order
        int size = components.size();
        int[] result = new int[size];
        for (int i = 0; i < size; i++) {
            // Read from the back of the list to ensure descending order
            result[i] = components.get(size - 1 - i);
        }
        
        return result;
    }
}