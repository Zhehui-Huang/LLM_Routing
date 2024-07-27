import math

def euclidean_distance(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

def verify_tour_and_cost(tour, cities, reported_cost):
    # Check Requirement 1: Start and end at the depot (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Visit each city exactly once (except depot)
    unique_cities = set(tour)
    if unique_cities != set(range(len(cities))):
        return "FAIL"
    
    # Check Requirement 3: Correct calculation of total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        city_a = cities[tour[i]]
        city_b = cities[tour[i + 1]]
        total_cost += euclidean_distance(city_a, city_b)
    
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-4):  # Using a tolerance to account for floating-point precision
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities_coordinates = [
    (53, 68),  # City 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Provided solution tour and cost
solution_tour = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
reported_cost = 278.9348447394249

# Verify the solution
verification_result = verify_tour_and_cost(solution_tour, cities_coordinates, reported_cost)
print(verification_result)