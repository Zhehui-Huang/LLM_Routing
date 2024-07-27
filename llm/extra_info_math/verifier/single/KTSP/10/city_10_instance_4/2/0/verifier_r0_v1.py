import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, reported_cost, cities):
    """Check if the solution meets the given requirements."""
    # Requirement 1: Start and end at depot city, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly 8 cities including the depot city
    unique_cities = set(tour)
    if len(unique_cities) != 8 or 0 not in unique_cities:
        return "FAIL"
    
    # Calculate the total travel distance
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Requirement 3: The tour’s total travel cost should be minimized and match the reported cost
    if not math.isclose(total_calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# List of city coordinates
cities = [
    (79, 15), # City 0: Depot
    (79, 55), # City 1
    (4, 80),  # City 2
    (65, 26), # City 3
    (92, 9),  # City 4
    (83, 61), # City 5
    (22, 21), # City 6
    (97, 70), # City 7
    (20, 99), # City 8
    (66, 62), # City 9
]

# Tour provided as an example solution
tour = [0, 2, 8, 9, 5, 1, 3, 4, 0]
reported_cost = 186.54

# Validate the provided solution
result = verify_solution(tour, reported_cost, cities)
print(result)