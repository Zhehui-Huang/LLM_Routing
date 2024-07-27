import math

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def verify_solution(tour, cost, cities):
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at depot city (0)."
    
    # Requirement 2: Visit each city exactly once
    if len(set(tour[1:-1])) != len(tour[1:-1]):
        return "FAIL: Not all cities are visited exactly once."
    
    # Requirement 5: Tour begins and ends at depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL: Tour does not begin and end correctly."
    
    # Requirement 3 & 6: Correct travel cost calculation
    calculated_cost = total_travel_cost(tour, cities)
    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return f"FAIL: Incorrect total travel cost. Expected {calculated_cost}, got {cost}."

    # Check if all cities are visited (requirement 2 continued)
    visited_cities = set(tour[1:-1])
    if visited_cities != set(range(1, len(cities))):
        return "FAIL: Not all cities are visited."
    
    return "CORRECT"

# Example data
cities = [
    (79, 15),  # Depot City 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
reported_cost = 320.7939094250147

# Verify the provided solution
result = verify_solution(tour, reported_success, cities)
print(result)