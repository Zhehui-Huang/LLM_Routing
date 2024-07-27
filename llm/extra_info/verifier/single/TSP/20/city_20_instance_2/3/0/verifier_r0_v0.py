import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities, expected_cost):
    if not tour:
        return "FAIL"
    
    # [Requirement 2]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 3]
    if len(set(tour)) != len(cities) or set(tour) != set(range(len(cities))):
        return "FAIL"

    # Calculate total cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # [Requirement 4 & 6]
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-3):
        return "FAIL"

    return "CORRECT"

# Cities data
cities = [
    (3, 26),  # Depot city 0
    (85, 72), # City 1
    (67, 0),  # City 2
    (50, 99), # City 3
    (61, 89), # City 4
    (91, 56), # City 5
    (2, 65),  # City 6
    (38, 68), # City 7
    (3, 92),  # City 8
    (59, 8),  # City 9
    (30, 88), # City 10
    (30, 53), # City 11
    (11, 14), # City 12
    (52, 49), # City 13
    (18, 49), # City 14
    (64, 41), # City 15
    (28, 49), # City 16
    (91, 94), # City 17
    (51, 58), # City 18
    (30, 48)  # City 19
]

tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
reported_cost = 478.43

print(verify_tour(tour, cities, reported_cost))