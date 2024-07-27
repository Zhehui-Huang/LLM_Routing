import math

# City Coordinates
cities = [
    (3, 26),  # City 0 - Depot
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

# Provided solution details
tour_provided = [0, 14, 6, 8, 16, 11, 7, 10, 3, 4, 1, 17, 5, 18, 13, 15, 9, 2, 19, 12, 0]
total_cost_provided = 519.96
max_distance_provided = 60.61

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities, total_cost_provided, max_distance_provided):
    # Check if the tour starts and ends at the depot and includes all cities exactly once except for the depot
    if tour[0] != 0 or tour[-1] != 0 or sorted(tour[1:-1]) != sorted(range(1, len(cities))):
        return "FAIL"
    
    # Calculate total travel cost and max distance
    total_cost_calculated = 0
    max_distance_calculated = 0
    for i in range(1, len(tour)):
        distance = calculate_euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
        total_cost_calculated += distance
        if distance > max_distance_calculated:
            max_distance_calculated = distance
    
    # Check calculated costs against provided
    if not math.isclose(total_cost_calculated, total_cost_provided, rel_tol=1e-2) or \
       not math.isclose(max_distance_calculated, max_distance_provided, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Validate the solution
result = verify_solution(tour_provided, cities, total_cost_provided, max_distance_provided)
print(result)