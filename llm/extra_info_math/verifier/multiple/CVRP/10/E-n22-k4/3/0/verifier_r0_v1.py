import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(cities, demands, robot_tours, robot_costs, capacities):
    all_visited_cities = set()

    # Test 1: Each city is visited once, excluding the depot
    for tour in robot_tours:
        all_visited_cities.update(tour[1:-1])  # Exclude the depot
        # Test 2: Tours start and end at depot
        assert tour[0] == 0 and tour[-1] == 0, "FAIL: Tour must start and end at depot"

    assert all_visited_cities == set(range(1, len(cities))), "FAIL: Each city must be visited exactly once"

    # Test 3: Check capacities and compute costs
    total_calculated_cost = 0
    for tour, reported_cost, capacity in zip(robot_tours, robot_costs, capacities):
        load = sum(demands[city] for city in tour[1:])
        assert load <= capacity, "FAIL: Capacity exceeded for robot"

        route_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        total_calculated_cost += route_cost

        # Allowing a small rounding difference
        assert round(route_cost, 2) == round(reported_cost, 2), "FAIL: Route cost calculation differs"

    # Test 4: Check total real cost
    expected_total_cost = sum(robot_costs)
    assert round(total_calculated_cost, 2) == round(expected_total_cost, 2), "FAIL: Total costs do not match"

    return "CORRECT"

# Define the coordinates and demands of each city
cities = {0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
          5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
          10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
          15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
          20: (155, 185), 21: (139, 182)}
demands = {0: 0, 1: 1100, 2: 700, 3: 800, 4: 1400,
           5: 2100, 6: 400, 7: 800, 8: 100, 9: 500,
           10: 600, 11: 1200, 12: 1300, 13: 1300, 14: 300,
           15: 900, 16: 2100, 17: 1000, 18: 900, 19: 2500,
           20: 1800, 21: 700}
robot_tours = [
    [0, 13, 19, 16, 0],
    [0, 21, 17, 14, 20, 18, 15, 0],
    [0, 12, 9, 7, 5, 2, 10, 0],
    [0, 1, 6, 8, 3, 4, 11, 0]
]
robot_costs = [71.69, 134.16, 105.98, 142.49]
capacities = [6000, 6000, 6000, 6000]

# Run the test
result = verify_solution(cities, demands, robot_tours, robot_costs, capacities)
print(result)