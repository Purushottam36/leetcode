class Solution:
    def maximum69Number (self, num: int) -> int:
        # Convert the integer to a string to access digits by position
        num_str = str(num)
        
        # Replace only the first occurrence of '6' with '9'
        max_num_str = num_str.replace('6', '9', 1)
        
        # Convert back to an integer and return
        return int(max_num_str)