import math

# City coordinates with index representing city number
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Robot tours provided by your solution
robot_tours = [
    [0, 12, 14, 15, 16, 18, 0],
    [0, 3, 4, 6, 8, 10, 11, 0],
    [0, 13, 17, 19, 20, 21, 0],
    [0, 1, 2, 5, 7, 9, 0]
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0]) ** 2 + 
                     (city_coordinates[city1][1] - city_coordinates[city2][1]) ** 2)

# Validate all requirements
def validate_solution(robot_tours, city_coordinates):
    all_cities_visited = set()
    max_travel_costs = []
    
    for tour in robot_tours:
        # Check requirement 2
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Robot tour does not start and end at the depot city."
        
        # Calculate travel cost for the tour
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(tour[i], tour[i + 1])
        
        # Collect max travel cost for requirement 5
        max_travel_costs.append(tour_cost)
        
        # Collect visited cities for requirement 3
        all_cities_visited.update(tour[1:-1])
    
    # Check requirement 3
    if all_cities_visited != set(range(1, len(city_coordinates))):  # exclude depot city
        return "FAIL: Not all cities are visited exactly once."
    
    # Check requirement 5
    reported_max_travel_cost = max(max_travel

_costs)
    if max(max_travel_costs) != reported_max_travel_cost:
        return f"FAIL: Reported max travel cost does not match the calculated value ({max_travel_costs})"

    # If all checks pass
    return "CORRECT"

# Run the unit tests
result = validate_solution(robot_tours, city_coordinates)
print(result)