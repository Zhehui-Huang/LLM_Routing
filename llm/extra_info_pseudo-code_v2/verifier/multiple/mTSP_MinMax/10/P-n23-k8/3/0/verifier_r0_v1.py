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

# Reported costs
reported_costs = [
    148.5805595456585, 60.41929763304924, 108.14471739432173, 107.17593711044337, 
    73.3620278568309, 101.91419695208016, 70.31738766580068, 53.164232844945644
]

# Function to compute Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Validation function
def validate_solution(tours, reported_costs, city_coordinates):
    all_cities = set(range(1, len(city_coordinates)))  # Cities 1 to 22
    visited_cities = set()

    computed_costs = []
    for tour in tours:
        # Start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tours must start and end at the depot"

        cost = 0
        for i in range(len(tour) - 1):
            cost += distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
            if i > 0:  # ignore depot in visited cities count
                visited_cities.add(tour[i])
        computed_costs.append(cost)

    # Check all cities are visited exactly once
    if visited_cities != all_cities:
        return "FAIL: Each city must be visited exactly once"
    
    # Check reported and computed tour costs
    for i in range(len(reported_costs)):
        if not math.isclose(computed_costs[i], reported_costs[i], abs_tol=0.01):
            return f"FAIL: Cost mismatch for robot {i} ({computed_costs[i]} vs {reported_costs[i]})"

    # Check for the maximum cost minimization
    if not math.isclose(max(computed_costs), max(reported_costs), abs_tol=0.01):
        return "FAIL: Maximum cost error"

    return "CORRECT"

# Execute the validation
result = validate_race_conditions(tours, reported_costs, city_coordinates)
print(result)