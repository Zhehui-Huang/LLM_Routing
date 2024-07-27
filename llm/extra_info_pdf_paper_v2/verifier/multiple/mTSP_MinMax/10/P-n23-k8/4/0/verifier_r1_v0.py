import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
        20: (45, 35), 21: (32, 39), 22: (56, 37)
    }
    
    tours = [
        [0, 4, 7, 12, 0],
        [0, 17, 14, 18, 0],
        [0, 1, 16, 20, 0],
        [0, 5, 8, 22, 0],
        [0, 21, 10, 13, 0],
        [0, 3, 9, 6, 0],
        [0, 15, 11, 0],
        [0, 2, 19, 0]
    ]
    
    calculated_costs = [
        109.20,
        114.12,
        48.82,
        95.78,
        70.31,
        88.79,
        68.04,
        89.37
    ]
    
    # Test Requirement 2: Unique city visitation
    all_visited_cities = set()
    for tour in tours:
        visited_cities = set(tour)
        if (0 in visited_cities):
            visited_cities.remove(0)  # Remove depot from check for unique city visit
        all_visited_cities.update(visited_cities)
    
    if len(all_visited_cities) != 22:  # As city 0 (depot) is not counted
        print("FAIL: Not all cities are visited exactly once.")
        return
    
    # Test Requirement 3 & 6: Calculate distance and compare
    max_calculated_cost = 0
    for tour, expected_cost in zip(tours, calculated_costs):
        cost = 0
        for i in range(1, len(tour)):
            cost += calculate_distance(cities[tour[i-1]], cities[tour[i]])
        if not math.isclose(cost, expected_cost, abs_tol=0.01):
            print(f"FAIL: Incorrect total cost calculation for tour from depot {tour}.")
            return
        if cost > max_calculated_cost:
            max_calculated_cost = cost
    
    if not math.isclose(max_calculated_cost, 114.12, abs_tol=0.01):
        print("FAIL: Maximum travel cost is incorrect.")
        return
    
    # All validations passed
    print("CORRECT")

test_solution()