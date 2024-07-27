import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, total_cost, cities):
    # Verify requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify requirement 2
    if len(tour) != 7:  # include both starting and ending at the depot
        return "FAIL"
    
    # Compute the travel cost and verify against requirement 3
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check if your calculated cost closely matches the given total_cost
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities_coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Given solution
tour_solution = [0, 8, 5, 2, 1, 9, 0]
total_travel_cost_solution = 183.85

# Verify solution
result = verify_tour(tour_solution, total_travel_cost_solution, cities_coordinates)
print(result)