import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost):
    # Coordinates of the cities
    cities = [
        (50, 42),  # City 0 - Depot
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
    
    # [Requirement 1] Check if the tour starts and ends at Depot City (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Check if exactly 4 cities are visited
    if len(set(tour)) != 4:
        return "FAIL"

    # [Requirement 3] Check if the given tour cost is minimal
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Allow a small margin for floating-point precision issues
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided tour and its total travel cost
tour = [0, 9, 5, 6, 0]
total_travel_cost = 61.66

# Call the verification function
result = verify_solution(tour, total_travel_cost)
print(result)