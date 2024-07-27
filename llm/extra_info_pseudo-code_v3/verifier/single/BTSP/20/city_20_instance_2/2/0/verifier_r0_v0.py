import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_cost, max_distance):
    # Coordinates of the cities
    cities = {
        0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
        6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53),
        12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49), 
        17: (91, 94), 18: (51, 58), 19: (30, 48)
    }

    # [Requirement 1] Check starts and ends at depot, includes all cities once
    if tour[0] != 0 or tour[-1] != 0 or sorted(tour) != sorted(set(tour)) or len(tour) != 21:
        return "FAIL"
    
    # [Requirement 4] Calculate actual distances
    calculated_distances = [euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1)]
    
    # [Requirement 2] Check for minimizing the longest distance
    if not math.isclose(max(calculated_distances), max_distance, abs_tol=1e-2):
        return "FAIL"

    # [Requirement 3] Calculate total travel cost and check
    calculated_total_cost = sum(calculated_distances)
    if not math.isclose(calculated_total_cost, total_cost, abs_tol=1e-2):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Provided test case
tour = [0, 12, 14, 6, 8, 10, 3, 7, 11, 13, 16, 19, 18, 4, 17, 1, 5, 15, 9, 2, 0]
total_travel_cost = 519.51
max_distance_between_cities = 69.08

# Execute test
result = test_solution(tour, total_travel_cost, max_distance_between_cities)
print(result)