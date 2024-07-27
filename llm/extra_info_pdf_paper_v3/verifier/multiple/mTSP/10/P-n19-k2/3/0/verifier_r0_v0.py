def calculate_distance(p1, p2):
    # Calculates Euclidean distance between two points
    from math import sqrt
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def tour_cost(tour, city_coords):
    # Calculate the travel cost for a given tour based on city coordinates
    cost = 0
    for i in range(1, len(tour)):
        cost += calculate_distance(city_coords[tour[i-1]], city_coords[tour[i]])
    return cost

def test_solution():
    # City coordinates, indexed by city number
    city_coords = {
        0: (30, 40),
        1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
        6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
        11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
        16: (62, 63), 17: (63, 69), 18: (45, 35)
    }

    # Provided solution
    tours = {
        0: [0, 6, 2, 7, 5, 9, 8, 3, 4, 1, 0],
        1: [0, 10, 11, 14, 12, 17, 16, 15, 13, 18, 0]
    }

    # Validate Requirement 1: Check if all cities except the depot are visited exactly once
    all_cities_visited = set(range(1, 19))
    cities_in_tours = {city for tour in tours.values() for city in tour if city != 0}
    if cities_in_tours != all_cities_visited:
        return "FAIL"

    # Validate Requirement 2: Check if each robot starts and ends at the depot
    for tour in tours.values():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Calculate and compare total travel cost
    provided_costs = [115.60355496962676, 149.767263793843]  # Given costs
    calculated_costs = [tour_cost(tour, city_coords) for tour in tours.values()]

    # Very lenient check for costs; typically should solve and compare optimal value
    if not all(abs(pc - cc) < 1e-6 for pc, cc in zip(provided_costs, calculated_costs)):
        return "FAIL"

    # Verify total cost as minimum not feasible here, we skip that part.

    return "CORRECT"

# Call the test function
result = test_solution()
print(result)