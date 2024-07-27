import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, cities):
    # Check if tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once, excluding the depot
    visited = set(tour)
    required_cities = set(range(len(cities)))
    if visited != required_cities:
        return "FAIL"

    # Check if the travel distance matches the given total cost
    # Given total cost
    given_total_cost = 271.4716218753353
    
    # Calculate the total travel distance of the provided tour
    total_travel_distance = 0
    for i in range(len(tour) - 1):
        total_travel_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(total_travel_distance, given_total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Cities with their coordinates
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Proposed tour from input
proposed_tour = [0, 5, 9, 4, 8, 3, 2, 1, 6, 7, 0]

# Verify the tour
result = verify_tour(proposed_tour, cities)
print(result)