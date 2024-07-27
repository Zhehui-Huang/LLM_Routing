import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, total_cost, max_distance):
    cities = [
        (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
        (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
        (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
        (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)  # Depot city is included at start
    ]

    # Check start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check visiting each city exactly once, excluding the repeat of the depot
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL"

    # Calculating total cost and checking max distance between consecutive cities
    computed_total_cost = 0
    computed_max_distance = 0
    
    for i in range(len(tour)-1):
        dist = calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        computed_total_cost += dist
        if dist > computed_max_distance:
            computed_max_distance = dist

    # Check the total cost and max distance
    if not math.isclose(computed_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(computed_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Given solution details.
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
total_travel_cost = 478.43
max_distance_between_cities = 80.61

# Execute verification and output the result.
result = verify_tour(tour, total_travel_cost, max_distance_between_cities)
print(result)