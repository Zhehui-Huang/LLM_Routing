import math

# Provided solution details
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 14, 8, 12, 18, 0]
total_travel_cost = 426.00
maximum_distance_between_consecutive_cities = 41.00

# Coordinates of the cities as provided in the task description
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), 
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), 
    (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), 
    (53, 76), (19, 72)
]

def compute_distance(city1, city2):
    """Compute the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_requirements(tour, cities):
    """Verify requirements based on the provided solution."""
    # Requirement 1: Start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city visited exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) + 1 or not all(city in unique_cities for city in range(len(cities))):
        return "FAIL"
    
    # Calculate the actual distances and total travel cost
    actual_total_cost = sum(compute_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    max_consecutive_distance = max(compute_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    
    # Requirement 3: Check total travel cost and the maximum distance
    if not math.isclose(actual_total_cost, total_travel_cost, abs_tol=1e-2):
        return "FAIL"
    if not math.isclose(max_consecutive_distance, maximum_distance_between_consecutive_cities, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Validate the solution
result = verify_requirements(tour, cities)
print(result)