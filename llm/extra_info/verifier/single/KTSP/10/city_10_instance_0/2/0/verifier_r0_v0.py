import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities, reported_cost):
    # [Requirement 1] Check if the tour starts and ends at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if exactly 4 distinct cities are visited, including the depot.
    if len(set(tour)) != 4 or len(tour) != 5:
        return "FAIL"
    
    # [Requirement 3] Calculate and compare the travel cost as the Euclidean distance.
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
 
    if not math.isclose(total_calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# City coordinates, indexed accordingly.
cities = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Solution provided
tour_solution = [0, 5, 6, 9, 0]
total_travel_cost_solution = 65.2

# Verify the provided solution
result = verify_solution(tour_solution, cities, total_travel_count_solution)
print(result)