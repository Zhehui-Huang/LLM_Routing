import numpy as np

# Define the city coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182),
}

# Convert tours from the response, removing np.int64 and fixing formatting
tours = {
    0: [0, 7, 5, 9, 10, 8, 6, 4, 11, 0],
    1: [1, 12, 15, 14, 13, 1],
    2: [2, 16, 17, 2],
    3: [3, 19, 21, 20, 18, 3]
}

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to validate the solution and generate the required tests
def validate_solution(tours, cities):
    visited_cities = set()
    calculated_costs = []
    
    try:
        for robot_id, tour in tours.items():
            # Requirement 2: Check if each tour starts and ends at the robot's depot
            assert tour[0] == tour[-1] == robot_id, "Robot does not start and end at its depot"
            
            # Add visited cities (excluding depot start/end)
            visited_cities.update(tour[1:-1])
            
            # Calculate the travel cost
            total_cost = 0
            for i in range(len(tour) - 1):
                total_cost += calculate_distance(tour[i], tour[i + 1])
            calculated_costs.append(total_cost)
        
        # Requirement 3: Check if all cities are visited exactly once
        assert len(visited_cities) == 22, "Each city must be visited exactly once"

        # Requirement 6: Check total tour cost matches expected total cost
        overall_cost = sum(calculated_costs)
        expected_overall_cost = 610.4645696118977  # Since it's a float we consider a small epsilon for comparison
        assert abs(overall_cost - expected_overall_cost) < 1e-6, "Total calculated cost does not match the expected cost"
        
        return "CORRECT"
    except AssertionError as e:
        return f"FAIL: {str(e)}"

# Validate and output the result
result = validate_solution(tours, cities)
print(result)