import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define the cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Provided robot tours
robot_tours = {
    0: [0, 9, 6, 11, 13, 16, 0],
    1: [0, 1, 2, 5, 10, 8, 0],
    2: [0, 15, 21, 17, 14, 12, 0],
    3: [0, 4, 3, 18, 20, 19, 0]
}

# Provided travel costs for verification
provided_costs = {
    0: 112.1129145924931,
    1: 127.08972485045346,
    2: 109.58656514674047,
    3: 182.25865681509563
}

# Calculate the total cost and check tours
def verify_solution(tours, provided_costs):
    total_calculated_cost = 0
    all_visited_cities = set()

    for robot_id, tour in tours.items():
        tour_cost = 0
        visited_cities = set(tour)
        all_visited_cities.update(visited_cities)

        # Ensure the tour starts and ends at the depot (Requirement 5)
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        for i in range(len(tour) - 1):
            # Calculate and sum up travel costs (Requirement 4)
            tour_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        
        # Compare calculated tour cost to provided tour cost
        if not math.isclose(tour_cost, provided_costs[robot_id], rel_tol=1e-5):
            return "FAIL"

        total_calculated_cost += tour_cost

    # Check all cities are visited exactly once (Requirements 1 and 8)
    if len(all_visited_cities) != 22 or any(tour.count(city) > 1 for city in all_visited_cities for tour in tours.values()):
        return "FAIL"

    # Ensure minimum total travel cost is attempted (Requirement 3 - Not strictly verifiable but checked through provided cost)
    expected_total_cost = sum(provided_costs.values())
    if not math.isclose(total_calculated_cost, expected_total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Execute verification
result = verify_solution(robot_tours, provided_costs)
print(result)