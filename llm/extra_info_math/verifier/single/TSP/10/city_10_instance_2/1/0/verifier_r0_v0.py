import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cost, cities):
    # [Requirement 1] Start and end at depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Each city visited exactly once, except depot
    visited = set(tour)
    if len(visited) != len(cities) or set(range(len(cities))) != visited:
        return "FAIL"

    # [Requirement 3 & 4] Calculate travel cost using Euclidean distance and check if it matches provided cost
    calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, cost, abs_tol=0.1):  # Allowing small floating point tolerance
        return "FAIL"
    
    # [Requirement 5] Check for subtours
    # If there are no repeated cities in the path except for the starting/ending city, there is no subtour
    if len(tour) != len(set(tour)) + 1:  # +1 is for the starting city appearing again at the end
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [
    (90, 3),  # City 0 (Depot)
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Provided solution
tour = [0, 3, 0]
total_travel_cost = 156.32018423735306

# Verification
result = verify_solution(tour, total_travel_posit, cities)
print(result)