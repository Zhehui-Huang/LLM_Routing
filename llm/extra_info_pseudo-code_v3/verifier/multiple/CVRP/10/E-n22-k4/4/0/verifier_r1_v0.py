import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 
    14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

demands = {
    0: 0, 1: 1100, 2: 700, 3: 800, 4: 1400, 5: 2100, 6: 400, 7: 800, 
    8: 100, 9: 500, 10: 600, 11: 1200, 12: 1300, 13: 1300, 14: 300, 
    15: 900, 16: 2100, 17: 1000, 18: 900, 19: 2500, 20: 1800, 21: 700
}

# Robots solution provided
robots_tours = [
    [0, 14, 16, 17, 20, 21, 8, 0],
    [0, 14, 16, 17, 20, 21, 8, 0],
    [0, 14, 16, 17, 20, 21, 8, 0],
    [0, 14, 16, 17, 20, 21, 8, 0]
]

capacity = 6000
robot_costs = [135.6322487935778] * 4

def test_cvrp_solution(robots_tours, robot_costs):
    all_cities_visited = set()
    overall_travel_cost = 0

    for index, tour in enumerate(robots_tours):
        previous_city = tour[0]
        total_cost = 0
        total_demand = 0

        for city in tour[1:]:
            # Check for correct tour structure
            if city != 0 and previous_city == 0:
                return "FAIL"  # Starting city should be depot 0 once for a complete tour

            if not city in all_cities_visited:
                all_cities_visited.add(city)

            # Total demand calculation
            total_demand += demands[city]

            # Distance calculation
            dist = calculate_distance(*cities[previous_city], *cities[city])
            total_cost += dist
            previous_city = city

        # Check if ending at the depot
        if tour[-1] != 0:
            return "FAIL"

        # Check costs are as expected
        if not math.isclose(total_cost, robot_costs[index], rel_tol=1e-9):
            return "FAIL"

        # Check capacity constraint
        if total_demand > capacity:
            return "FAIL"

        overall_travel_cost += total_cost

    if not math.isclose(overall_travel_cost, sum(robot_costs), rel_tol=1e-9):
        return "FAIL"

    if len(all_cities_visited) != 22:  # All cities including depot must be visited
        return "FAIL"

    return "CORRECT"

print(test_cvrp_solution(robots_tours, robot_costs))