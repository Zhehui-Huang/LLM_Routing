import math

# Coordinates for each city including depots
coordinates = [
    (30, 40),  # Depot 0
    (37, 52),  # Depot 1
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Provided Tours
solution_tours = [
    [0, 16, 8, 18, 12, 10, 19, 20, 17, 14, 0],  # Robot 0 Tour
    [0, 4, 2, 7, 3, 15, 5, 9, 13, 6, 1],        # Robot 1 Tour
    [0, 11, 0]                                  # Robot 2 Tour
]

solution_costs = [
    185.37059520437924,  # Robot 0 Cost
    180.79373267104845,  # Robot 1 Cost
    56.32051136131489    # Robot 2 Cost
]

overall_total_cost = 422.48483923674263

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Generate tests to validate provided solution

def test_robot_tours():
    visited_cities = set()
    total_calculated_cost = 0
    
    for i, tour in enumerate(solution_tours):
        tour_cost = 0
        last_city = tour[0]
        visited_cities.add(last_city)
        
        # Ensure the tour starts and ends with the same depot
        if tour[0] != tour[-1]:
            return "FAIL: The tour should start and end with the same depot"
        
        # Calculate travel cost and validate all cities visited once
        for city in tour[1:]:
            if city in visited_cities and city != tour[-1]:  # exclude last city check if it is the depot
                return "FAIL: City visited more than once"
            visited_cities.add(city)
            tour_cost += calculate_distance(coordinates[last_city], coordinates[city])
            last_city = city
        
        # Check if tour cost matches expected cost within a small margin (as cost is floating-point)
        if not math.isclose(tour_cost, solution_costs[i], abs_tol=1e-5):
            return "FAIL: Travel cost mismatch"
        
        total_calculated_cost += tour_cost
    
    # All cities exactly once validation
    if visited_cities != set(range(21)):
        return "FAIL: Not all cities visited exactly once"
        
    # Check if overall cost matches
    if not math.isclose(total_calculated_cost, overall_total_cost, abs_tol=1e-5):
        return "FAIL: Overall cost mismatch"
    
    return "CORRECT"

# Run the test
result = test_robot_tours()
print(result)