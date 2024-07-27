import math

# Provided solution data
robots_tours = {
    0: [0, 13, 17, 21, 9, 5, 1, 0],
    1: [0, 14, 18, 10, 6, 2, 0],
    2: [0, 15, 7, 3, 11, 19, 0],
    3: [0, 16, 12, 8, 4, 20, 0]
}
robots_costs = {
    0: 197.56,
    1: 154.73,
    2: 183.25,
    3: 177.49
}

# City coordinates including depot
city_coords = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Calculate Euclidean distance between two cities by their indices
def euclidean_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

# Check for each robot
all_cities_covered = set()
calculated_costs = {}
for robot_id, tour in robots_tours.items():
    cost = 0
    previous_city = tour[0]
    for city in tour[1:]:
        cost += euclidean_distance(previous_city, city)
        previous_city = city
    calculated_costs[robot_id] = round(cost, 2)
    all_cities_covered.update(tour)

# Test Results
def evaluate_tours_and_costs():
    # Requirement 3: All cities visited exactly once
    if len(all_cities_covered) != len(city_coords):
        return "FAIL"
    # Requirement 6: Verify costs
    for robot_id, cost in robots_costs.items():
        if abs(cost - calculated_costs[robot_id]) > 0.01:
            return "FAIL"
    
    # Sum of all tour costs
    total_cost_calculated = sum(calculated_costs.values())
    total_cost_provided = sum(robots_costs.values())
    if abs(total_cost_calculated - total_cost_provided) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# Run the evaluation procedure
print(evaluate_tours_and_costs())