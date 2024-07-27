import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_solution(tour, cities, total_travel_cost, max_distance):
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city visited exactly once
    if sorted(tour) != sorted(list(set(tour))):
        return "FAIL"
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL"

    # Calculate the total travel cost and maximum distance from the tour provided
    calc_total_cost = 0
    calc_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calc_total_cost += distance
        calc_max_distance = max(calc_max_return, distance)

    # Requirement 6: Check the total travel cost
    if not math.isclose(calc_total_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Requirement 7: Check the maximum distance between consecutive cities
    if not math.isclose(calc_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# City coordinates (indexed by city index)
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Provided solution details
tour = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 12, 14, 19, 18, 13, 9, 2, 15, 5, 1, 4, 17, 3, 7, 6, 8, 10, 11, 0]
total_travel_cost = 592.9134744569473
max_distance = 41.593268686170845

# Run the test
result = validate_solution(tour, cities, total_travel_code, max_in_response)
print(result)