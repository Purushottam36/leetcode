class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        answer = []
        depth = 0
        
        for char in seq:
            if char == '(':
                # Increase depth for the incoming opening parenthesis
                depth += 1
                # Distribute based on parity: odd depths to A (0), even to B (1)
                answer.append(0 if depth % 2 != 0 else 1)
            else:
                # Distribute the closing parenthesis matching the current depth
                answer.append(0 if depth % 2 != 0 else 1)
                # Decrease depth as the parenthesis pair closes
                depth -= 1
                
        return answer