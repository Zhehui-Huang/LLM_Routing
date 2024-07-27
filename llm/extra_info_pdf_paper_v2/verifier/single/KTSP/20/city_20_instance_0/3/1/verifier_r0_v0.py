import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_tour(cities, tour, expected_cost):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 4 cities are visited
    if len(tour) != 5:  # includes the return to the depot, hence 5 entries
        return "FAIL"
    
    # Calculate and verify the total travel cost
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Cities coordinates
cities_coordinates = {
    0: (8, 11),
    1: (40, 6),
    8: (61, 16),
    4: (25, 18)
}

# Provided tour and total cost
tour = [0, 1, 8, 4, 0]
provided_total_cost = 110.08796524611944

# Verification
result = verify_tour(cities_coordinates, tour, provided_total_cost)
print(result)