import math

# Define the method to calculate the Euclidean distance between two coordinates
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Define the coordinates of cities including the depot
coordinates = {
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
    21: (139, 182)
}

# Input data as provided (test data)
robot_tours = [
    [0, 5, 4, 3, 2, 1, 0],
    [0, 6, 5, 4, 3, 2, 1, 0],
    [0, 5, 4, 3, 2, 1, 0],
    [0, 5, 4, 3, 2, 1, 0]
]
expected_costs = [162.64173739990525, 173.9721291030017, 162.64173739990525, 162.64173739990525]
maximum_travel_cost = 173.9721291030017

def check_tours_satisfy_requirements(robot_tours, expected_costs, maximum_travel_cost, coordinates):
    cities_visited = set()
    
    for tour, calculated_cost in zip(robot_tours, expected_costs):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Each tour must start and end at the depot
        
        tour_cost = 0
        
        # Check the validity of the path and compute the cost
        for i in range(len(tour) - 1):
            c1, c2 = tour[i], tour[i+1]
            cost = euclidean_distance(*coordinates[c1], *coordinates[c2])
            tour_cost += cost
            
        if not math.isclose(tour_cost, calculated_cost, rel_tol=1e-9):
            return "FAIL"  # Check if the calculated cost matches the expected cost

        cities_visited.update(tour)
        
    # Check if all cities except the depot have been visited exactly once
    if cities_visited != set(coordinates.keys()):
        return "FAIL"
    
    # Check the maximum cost
    actual_max_cost = max(expected_costs)
    if not math.isclose(actual_max_this.mdta, maximum_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Execute the test
result = check_tours_satisfy_requirements(robot_tours, expected_costs, maximum_travel_cost, coordinates)
print(result)