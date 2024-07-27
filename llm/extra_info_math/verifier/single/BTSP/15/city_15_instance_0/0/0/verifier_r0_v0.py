def verify_solution(tour, total_travel_cost, max_distance):
    # [Requirement 1] Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Visit each city exactly once
    # Note: As city 0 is the depot and start and end point, it will appear twice in the valid tour.
    # All other cities should appear exactly once.
    from collections import Counter
    city_count = Counter(tour)
    if city_count[0] != 2 or any(city_count[city] != 1 for city in range(1, 15)):
        return "FAIL"

    # Calculate total distance and verify max distance
    # City coordinates
    cities = {
        0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
        6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65),
        11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
    }

    from math import sqrt

    def distance(c1, c2):
        # Euclidean distance calculation
        return sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)
    
    computed_total_cost = 0
    computed_max_distance = 0
    
    # Iterate through the tour and calculate distances between consecutive cities
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i + 1])
        computed_total_cost += dist
        if dist > computed_max_distance:
            computed_max_distance = dist

    # Check consistency with the provided cost and maximum distance
    if abs(computed_total_cost - total_travel_cost) > 0.1 or abs(computed_max_distance - max_distance) > 0.1:
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour = [0, 8, 9, 12, 11, 1, 14, 4, 7, 3, 5, 2, 6, 13, 10, 0]
total_travel_cost = 402.83
max_distance = 42.38

# Testing the solution
result = verify_solution(tour, total_travel_cost, max_distance)
print(result)