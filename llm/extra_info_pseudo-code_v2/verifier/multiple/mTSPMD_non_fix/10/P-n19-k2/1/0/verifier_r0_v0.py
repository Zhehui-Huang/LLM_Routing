import numpy as np

# Coordinates for each city indexed from 0 to 18
city_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(tour, num_cities):
    """Verify if the solution meets given constraints."""
    try:
        # Convert solutions to more manageable format for processing
        tour = np.array(tour, dtype=int)

        # Check if each city is visited exactly once
        unique_cities = set(tour[tour >= 0])  # remove negative numbers used for depot transitions
        if len(unique_cities) != num_cities:
            return "FAIL: Not all cities are visited exactly once."
        
        # Calculate total travel cost and verify distances
        previous_city = tour[0]
        total_cost = 0.0
        for city in tour[1:]:
            if city < 0:
                continue  # ignore depot indicators
            total_cost += calculate_distance(previous_city, city)
            previous_city = city
        
        if total_cost == float('inf'):
            return "FAIL: Invalid total cost (infinity)."
        
        return "CORRECT"  # If all checks pass, the solution is considered correct
    except Exception as e:
        return f"FAIL: Error encountered during validation: {str(e)}"

# Output from the solution given
robot_0_tour = [
    0, 17, 14, 13, 7, 9, 11, 4, 6, 2, 18, 8, 12, 16, 0, 15, 0, 3, 3, 10, 7, 2
]

# Call verify function to test the solution
result = verify_solution(robot_0_tour, 19)
print(result)