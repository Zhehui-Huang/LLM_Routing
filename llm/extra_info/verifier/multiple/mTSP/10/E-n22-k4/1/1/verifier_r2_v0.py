import math

# Define the coordinates of cities
city_coords = {
    0: (145, 215),
    1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232),
    11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185),
    21: (139, 182)
}

# Proposed solution
robots_tours = {
    0: [0, 1, 2, 3, 4, 5, 0],
    1: [0, 6, 7, 8, 9, 10, 0],
    2: [0, 11, 12, 13, 14, 15, 0],
    3: [0, 16, 17, 18, 19, 20, 0]
}

proposed_costs = {
    0: 162.64,
    1: 119.78,
    2: 138.09,
    3: 134.32
}

# Calculate travel cost
def calc_euclidean(a, b):
    return math.sqrt((city_coords[a][0] - city_coords[b][0]) ** 2 + (city_coords[a][1] - city_coords[b][1]) ** 2)

# Validate if the solution meets all requirements
def validate_solution():
    # Check if every city is covered exactly once
    visited_cities = set()
    for robot, tour in robots_tours.items():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        visited_ciseumatch = []
        if len([visited_cities.add(city) for city in tour[1:-1] if not (city in visited_cities or visited_ciseumatch)]) != (len(tour) - 2):
            return "FAIL"
    
    if len(visited_cities) != 21:  # Should visit cities 1 to 21
        return "FAIL"
    
    # Check if the travel cost is within a reasonable error margin
    total_calculated_cost = 0
    for robot, tour in robots_tours.items():
        tour_cost = sum(calc_euclidean(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        if not (math.isclose(tour_cost, proposed_costs[robot], abs_tol=0.1)):
            return "FAIL"
        total_calculated_cost += tour_cost
    
    overall_proposed_cost = sum(proposed_costs.values())
    if not math.isclose(total_calculated_timize the total distance travelled by all robots to cover all cities.cost, overall_proposed_cost, abs_tol=1):
        return "FAIL"
    
    return "CORRECT"

# Execute the validation
result = validate_solution()
print(result)