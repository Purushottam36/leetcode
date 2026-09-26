class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        #Create a hash map for O(1) key lookups
        lookup = {key: val for key, val in knowledge}
        
        res = []
        current_key = []
        is_inside = False
        
        #Iterate through the string to extract and replace bracket pairs
        for char in s:
            if char == '(':
                is_inside = True
            elif char == ')':
                is_inside = False
                key_str = "".join(current_key)
                # Append the value if found, otherwise append '?'
                res.append(lookup.get(key_str, '?'))
                current_key = []
            else:
                if is_inside:
                    current_key.append(char)
                else:
                    res.append(char)
                    
        return "".join(res)