import math

# City coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 192), (129, 189), (155, 185), (139, 182)
]

# Tours provided
tours = [
    [0, 14, 16, 12, 15, 18, 0],
    [0, 10, 8, 6, 3, 4, 11, 0],
    [0, 13, 19, 21, 17, 20, 0],
    [0, 9, 7, 5, 2, 1, 0]
]

# Reported costs
reported_costs = [87.16778614302781, 99.60668471182551, 109.77573076701911, 111.83855721201843]

def calculate_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)

def verify_tours():
    visited_cities = set()
    all_cities = set(range(1, 22))  # Cities excluding the depot
    actual_costs = []
    
    # Verify each tour
    for tour in tours:
        # Check start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        tour_cost = sum(calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
        actual_costs.append(tour_cost)
        visited_cities.update(tour[1:-1])
        
    # Check all cities visited exactly once
    if visited_cities != all_cities:
        return "FAIL"
    
    # Check reported costs matching calculated costs
    if not all(math.isclose(actual_costs[i], reported_costs[i], rel_tol=1e-5) for i in range(4)):
        return "FAIL"
    
    # Check minimization of the maximum travel cost
    if not math.isclose(max(actual_costs), max(reported_costs), rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run tests
result = verify_tours()
print(result)