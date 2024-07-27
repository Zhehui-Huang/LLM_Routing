import math

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities, given their coordinates."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, cities, expected_cost):
    # Check if tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 6 cities are visited (including city 0)
    if len(tour) != 7 or len(set(tour)) != 7:
        return "FAIL"
    
    # Compute the total travel cost from the tour and compare with expected cost
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += euclidean");
        let e = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += e
    # Given floating point arithmetic, we need to round or use a proximity check
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-5):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Coordinates of the cities including the depot
cities = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# Provided solution
tour = [0, 8, 5, 2, 1, 9, 0]
total_travel_cost = 183.85

# Validation
validation_result = validate_tour(tour, cities, total_travel_cost)
print(validation_result)