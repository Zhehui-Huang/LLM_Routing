import math

# City coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Tours reported
tours = [
    [0, 14, 4, 17, 0],
    [0, 21, 5, 2, 0],
    [0, 11, 19, 16, 0],
    [0, 10, 9, 12, 0],
    [0, 8, 3, 1, 0],
    [0, 18, 7, 13, 0],
    [0, 6, 15, 0],
    [0, 20, 22, 0]
]

# Actual costs reported vs. computed
reported_costs = [
    148.5805595456585, 60.41929763304924, 108.14471739432173, 107.17593711044337, 
    73.3620278568309, 101.91419695208016, 70.31738766580068, 53.164232844945644
]

# Compute Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Check requirements and validate
def validate_solution(tours, reported_costs, city_coordinates):
    all_cities = set(range(1, len(city_coordinates)))  # All cities except depot as sets {1, 2, ..., 22}
    visited_cities = set()

    computed_costs = []
    for tour in tours:
        # Starting and ending at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tours must start and end at the depot"
        
        # Compute and compare tour costs
        cost = 0
        for i in range(len(tour) - 1):
            cost += distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
            if i > 0:  # don't include the depot as a visited city
                visited_cities.add(tour[i])

        computed_costs.append(cost)

    # Check if each non-depot city is visited exactly once
    if visited_cities != all_cities:
        return "FAIL: All cities must be visited exactly once"

    # Check reported costs accuracy
    if not all(math.isclose(reported_costs[i], computed_costs[i], abs_tol=0.01) for i in range(len(reported_costs))):
        return "FAIL: Reported travel costs do not match computed ones"

    # Primary goal: minimized maximum distance traveled
    reported_max_cost = max(reported_costs)
    if not math.isclose(reported_max_cost, max(computed_costs), abs_tol=0.01):
        return "FAIL: Maximum travel cost error"

    # If every check is passed
    return "CORRECT"

# Validation
result = validate_solution(tours, reported_costs, city_sq_coordinates)
print(result)