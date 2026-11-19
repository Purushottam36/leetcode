class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # Split into real and imaginary parts
        real1_str, imag1_str = num1[:-1].split('+')
        real2_str, imag2_str = num2[:-1].split('+')
        
        # Convert strings to integers
        a, b = int(real1_str), int(imag1_str)
        c, d = int(real2_str), int(imag2_str)
        
        # Calculate the resulting real and imaginary parts
        real_part = (a * c) - (b * d)
        imag_part = (a * d) + (b * c)
        
        return f"{real_part}+{imag_part}i"