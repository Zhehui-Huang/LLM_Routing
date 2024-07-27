import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(cities, tour, total_cost, max_distance):
    # Verify the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify all cities are visited exactly once, excluding the start/end at the depot
    if sorted(tour[1:-1]) != sorted(range(1, len(cities))):
        return "FAIL"

    # Calculate the total travel cost and maximum distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]][0], cities[tour[i]][1], cities[tour[i+1]][0], cities[tour[i+1]][1])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist

    # Compare calculated costs and distances with provided values
    if not (math.isclose(calculated_total_cost, total_cost, rel_tol=1e-2) and
            math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2)):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [
    (3, 26),   # Depot city 0
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

# Provided solution
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
total_travel_cost = 478.43
maximum_distance_between_cities = 80.61

# Run verification
result = verify_solution(cities, tour, total_travel_cost, maximum_distance_between_cities)
print(result)