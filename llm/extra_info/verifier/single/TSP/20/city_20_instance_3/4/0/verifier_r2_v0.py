import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, total_travel_cost):
    # Coordinates of the cities
    cities = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
        (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
        (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    
    # Check Requirement 1: Starts and ends at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: All cities must be visited exactly once, except depot
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != len(cities) - 1 or any(city not in visited_cities for city in range(1, len(cities))):
        return "FAIL"
    
    # Check Requirement 3: Correct calculation of total travel cost
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        total_calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Using a tolerance due to floating point arithmetic issues
    if not math.isclose(total_calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Check Requirement 4 and 5 implicitly satisfied by parameters and given result check
    return "CORRECT"

# Example solution
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
total_travel_cost = 458.36719998557066

# Validate the provided tour and cost
result = verify_tour(tour, total_travel_cost)
print(result)