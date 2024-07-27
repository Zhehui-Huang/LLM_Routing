import math

# Coordinates for each city including the depot
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# List of tours assigned to each robot
tours = [
    [0, 14, 10, 8, 6, 5, 1, 0],
    [0, 16, 15, 9, 7, 4, 0],
    [0, 12, 17, 18, 20, 3, 0],
    [0, 13, 11, 19, 21, 2, 0]
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Validator function to check if the solution meets all the requirements
def validate_solution(tours, city_coordinates):
    city_count = len(city_coordinates)
    all_visited = set()
    max_distance = 0
    
    for tour in tours:
        # Check if the tour starts and ends at the depot (Requirement 2)
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start or end at depot"
        
        previous_node = tour[0]
        total_distance = 0
        for i in range(1, len(tour)):
            current_node = tour[i]
            distance = calculate_distance(city_coordinates[previous_node], city_coordinates[current_node])
            total_distance += distance
            all_visited.add(current_node)
            previous_node = current_node
        
        max_distance = max(max_distance, total_distance)
    
    # Check if all cities are visited exactly once (Requirement 4)
    if all_visited != set(range(1, city_count)):
        return "FAIL: Not all cities are visited or some are visited more than once"

    return "CORRECT"

# Execute validation and print the result
result = validate_solution(tours, city_coordinates)
print(result)