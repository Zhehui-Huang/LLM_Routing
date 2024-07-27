import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tours(city_coordinates, tours):
    # Check if each city is visited exactly once and tours start/end at the depot
    all_cities_visited = set()
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return False  # Tours must start and end at the depot
        for city in tour[1:-1]:  # skip the depot city at start and end
            if city in all_cities_visited:
                return False  # City visited more than once
            all_cities_visited.add(city)

    if len(all_cities_visited) != len(city_coordinates) - 1:  # minus the depot city
        return False  # Not all cities were visited

    # All cities except the depot should be visited exactly once
    return True

def verify_tour_costs(city_coordinates, tours, expected_costs):
    # Verify tour costs
    actual_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            cost += calculate_euclidean_distance(*city_coordinates[city1], *city_coordinates[city2])
        actual_costs.append(cost)

    # Check the costs rounded to an acceptable precision to avoid floating-point precision issues
    if not all(math.isclose(ac, ec, rel_tol=1e-9) for ac, ec in zip(actual_costs, expected_costs)):
        return False  # Costs do not match

    return True
    
def unit_test_solution():
    city_coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
        20: (45, 35)
    }
    
    tours = [
        [0, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 0], 
        [0, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 0]
    ]
    
    expected_costs = [143.98241284438606, 109.8362166450987]
    overall_cost_expected = 253.81862948948475
    
    if not verify_tours(city_coordinates, tours):
        return "FAIL"
    
    if not verify_tour_costs(city_coordinates, tours, expected_costs):
        return "FAIL"
    
    # Verify overall cost
    if not math.isclose(sum(expected_costs), overall_cost_expected, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Run the unit test
print(unit_test_solution())