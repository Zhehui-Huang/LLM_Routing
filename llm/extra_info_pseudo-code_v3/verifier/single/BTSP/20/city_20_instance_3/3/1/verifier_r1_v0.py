import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(cities, tour, expected_total_cost, expected_max_distance):
    if len(tour) != len(set(tour)):
        return "FAIL"  # Check for duplicates, thus ensuring each city is visited once

    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour must start and end at city 0

    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        cost = euclidean_distance(cities[tour[i]][0], cities[tour[i]][1], cities[tour[i+1]][0], cities[tour[i+1]][1])
        total_cost += cost
        if cost > max_distance:
            max_distance = cost

    # Compare calculated total travel cost and maximum distance with provided values
    if abs(total_cost - expected_total_traversal_cost) > 1e-2 or abs(max_distance - expected_max_distance) > 1e-2:
        return "FAIL"

    return "CORRECT"

cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

tour = [0, 1, 3, 5, 2, 6, 13, 19, 15, 17, 16, 9, 11, 10, 4, 7, 14, 8, 12, 18, 0]
expected_total_traversal_cost = 506.93
expected_max_distance = 41.00

result = verify_tour(cities, tour, expected_total_traversal_cost, expected_max_distance)
print(result)