from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tsp_vrp_solution():
    # Define cities by their coordinates
    cities = {
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

    # Robot tours configuration from the proposed solution
    robot_tours = {
        0: [0, 12, 14, 15, 16, 18, 0],
        1: [0, 3, 4, 6, 8, 10, 11, 0],
        2: [0, 13, 17, 19, 20, 21, 0],
        3: [0, 1, 2, 5, 7, 9, 0]
    }

    # Expected costs (as given)
    expected_costs = {
        0: 121.21,
        1: 124.24,
        2: 138.25,
        3: 111.84
    }

    overall_total_cost = 495.54

    # Verify each robot tour
    total_calculated_cost = 0

    cities_visited = set()
    for robot_id, tour in robot_tours.items():
        previous_city = tour[0]
        tour_cost = 0

        for city in tour[1:]:
            tour_cost += calculate_distance(cities[previous_city], cities[city])
            previous_city = city
            if city != 0:
                cities_visited.add(city)

        # Check if tour cost matches expected cost approximately
        if not (abs(tour_cost - expected_costs[robot_id]) < 0.5):
            return "FAIL"
        total_calculated_cost += tour_cost

    # Check if all non-depot cities are visited exactly once
    if len(cities_visited) != 21 or any(city == 0 for city in cities_visited):
        return "FAIL"

    # Check the summed costs
    if not (abs(total_calculated_cost - overall_total_cost) < 0.5):
        return "FAIL"
    
    return "CORRECT"

# Run the test on the given solution
print(test_tsp_vrp_solution())