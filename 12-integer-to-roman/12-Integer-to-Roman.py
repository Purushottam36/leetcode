class Solution:
    def intToRoman(self, num: int) -> str:
        # Define Roman numerals and their values from largest to smallest
        value_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
            (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
            (1, "I")
        ]
        
        result = []
        
        # Greedily match and subtract values
        for value, symbol in value_map:
            if num == 0:
                break
            count = num // value
            if count > 0:
                result.append(symbol * count)
                num %= value
                
        return "".join(result)