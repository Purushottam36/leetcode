class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        min_even = float('inf')
        has_odd = False
        
        for num in nums1:
            if num % 2 != 0:
                has_odd = True
                if num < min_odd:
                    min_odd = num
            else:
                if num < min_even:
                    min_even = num
                    
        # Condition 1: Can we make everything even? 
        # Only possible if there are no odd numbers to begin with.
        if not has_odd:
            return True
            
        # Condition 2: Can we make everything odd?
        # Possible if the smallest even number isn't stuck below the smallest odd number.
        if min_even > min_odd:
            return True
            
        return False