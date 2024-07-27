import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(cities, demands, robot_tours, capacities):
    robot_details = {
        0: {'tour': [0, 13, 19, 16, 0], 'cost': 71.69},
        1: {'tour': [0, 21, 17, 14, 20, 18, 15, 0], 'cost': 134.16},
        2: {'tour': [0, 12, 9, 7, 5, 2, 10, 0], 'cost': 105.98},
        3: {'tour': [0, 1, 6, 8, 3, 4, 11, 0], 'cost': 142.49},
    }
    expected_total_cost = 454.32
    all_visited_cities = set()

    # Test 1: Each city is visited once, excluding the depot (0)
    for details in robot_details.values():
        tour = details['tour']
        all_visited_cities.update(tour[1:-1])  # Exclude the depot
        # Test 2: Tours start and end at depot
        assert tour[0] == 0 and tour[-1] == 0, "FAIL: Tour must start and end at depot"

    assert all_visited_cities == set(range(1, len(cities))), "FAIL: Each city must be visited exactly once"

    # Test 3: Check capacities and compute costs
    total_calculated_cost = 0
    for robot_id, details in robot_details.items():
        tour = details['tour']
        cost = details['cost']
        load = 0
        route_cost = 0
        
        for i in range(len(tour) - 1):
            node = tour[i]
            next_node = tour[i + 1]
            load += demands[next_node]
            route_cost += calculate_distance(cities[node], cities[next_node])

        # Capacity check
        assert load <= capacities[robot_id], "FAIL: Capacity exceeded for robot"
        # Cost comparison (allow slight discrepancy due to rounding)
        assert round(route_cost, 2) == round(cost, 2), "FAIL: Calculated route cost does not match"

        total_calculated_cost += route_cost

    # Test 4: Check total cost
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
capacities = {0: 6000, 1: 6000, 2: 6000, 3: 6000}

# Run the test
result = verify_solution(cities, demands, robot_details, capacities)
print(result)