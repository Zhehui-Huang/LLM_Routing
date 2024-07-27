def calculate_euclidean_distance(city1, city2):
    import math
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    # City coordinates setup
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
        4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
        8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
        16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35)
    }
    
    # Provided tours and costs
    robot_tours = [
        [0, 1, 4, 10, 2, 3, 8, 9, 7, 5, 6, 0],
        [0, 16, 11, 15, 12, 19, 18, 13, 17, 14, 20, 0]
    ]
    reported_costs = [131.04, 145.76]
    expected_total_cost = 276.79
    
    calculated_costs = []
    all_visited_cities = set()
    
    # Check tours and calculate costs
    for tour in robot_tours:
        # Requirement 1: Check if each tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Requirement 4: Check tour format and depot start/end
        if tour.count(0) != 2:
            return "FAIL"
        
        # Calculate the total travel cost of the tour
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        
        calculated_costs.append(round(total_cost, 2))
        all_visited_cities.update(tour[1:-1])  # exclude the depot city

    # Requirement 2: Each city must be visited exactly once
    if len(all_visited_cities) != 20:
        return "FAIL"

    # Requirement 3 & 5: Minimize and calculate total travel costs
    if not all(abs(calc - real) < 0.01 for calc, real in zip(calculated_costs, reported_costs)):
        return "FAIL"
    if abs(sum(reported_costs) - expected_total result) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# Execute the test
print(test_solution())