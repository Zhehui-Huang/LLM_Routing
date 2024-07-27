import math

# Define the city coordinates
cities = [
    (3, 26),     # City 0
    (85, 72),    # City 1
    (67, 0),     # City 2
    (50, 99),    # City 3
    (61, 89),    # City 4
    (91, 56),    # City 5
    (2, 65),     # City 6
    (38, 68),    # City 7
    (3, 92),     # City 8
    (59, 8),     # City 9
    (30, 88),    # City 10
    (30, 53),    # City 11
    (11, 14),    # City 12
    (52, 49),    # City 13
    (18, 49),    # City 14
    (64, 34),    # City 15
    (28, 49),    # City 16
    (91, 94),    # City 17
    (51, 58),    # City 18
    (30, 48)     # City 19
]

# Given solution path and values
tour = [0, 14, 16, 19, 11, 7, 18, 13, 15, 9, 2, 5, 1, 17, 4, 3, 10, 8, 6, 12, 0]
total_travel_cost = 434.582905498429
max_distance_consecutive_cities = 60.92618484691127

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_tour(tour, cities):
    tour_length = len(tour)
    visited = set(tour)
    total_dist = 0
    max_dist = 0

    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once (except the depot which should be visited twice)
    if len(visited) != len(cities) or visited != set(range(len(cities))):
        return "FAIL"

    # Calculate total travel cost and max distance between consecutive cities
    for i in range(1, tour_length):
        dist = calculate_distance(cities[tour[i-1]], cities[tour[i]])
        total_dist += dist
        if dist > max_dist:
            max_dist = dist

    # Check if computed values match the given values
    if not (math.isclose(total_dist, total_travel_cost, rel_tol=1e-5) and
            math.isclose(max_dist, max_distance_consecutive_cities, rel_tol=1e-5)):
        return "FAIL"

    return "CORRECT"

# Execute the test
result = verify_tour(tour, cities)
print(result)