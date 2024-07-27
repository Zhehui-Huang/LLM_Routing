import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, cities):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at depot city 0."

    # Check if each city is visited exactly once
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL: Not all cities are visited exactly once."

    # Calculate total travel cost and maximum distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        max_distance = max(max_distance, dist)

    # Compare with provided solution details
    provided_total_cost = 503.93280249020313
    provided_max_distance = 96.1041102138717
    if abs(total_cost - provided_total_cost) > 1e-6:
        return "FAIL: Total travel cost does not match."
    if abs(max_distance - provided_max_distance) > 1e-6:
        return "FAIL: Maximum distance between consecutive cities does not match."

    return "CORRECT"

# Define city coordinates (including the depot)
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
          (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
          (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)]

# Tour provided in the solution
tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 6, 2, 9, 13, 8, 1, 15, 18, 17, 19, 12, 0]

# Verify the tour
result = verify_tour(tour, cities)
print(result)