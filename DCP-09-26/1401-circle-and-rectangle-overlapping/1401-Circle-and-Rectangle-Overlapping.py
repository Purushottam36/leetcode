class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Clamp the circle's center coordinates to the rectangle's boundaries, yields the point on or inside the rectangle closest to the circle's center.
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate the horizontal and vertical distance components
        distance_x = closest_x - xCenter
        distance_y = closest_y - yCenter
        
        # Compute the squared Euclidean distance
        squared_distance = (distance_x * distance_x) + (distance_y * distance_y)
        
        # If the squared distance is less than or equal to radius^2, they overlap
        return squared_distance <= radius * radius