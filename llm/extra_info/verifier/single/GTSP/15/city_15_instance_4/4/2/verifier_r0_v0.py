import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, city_groups, cities, total_travel_cost):
    # Requirement 1: Start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit exactly one city from each group
    visited_groups = [False] * len(city_groups)
    for city in tour[1:-1]:  # Ignore the depot at start and end
        found_group = False
        for idx, group in enumerate(city_groups):
            if city in group:
                if visited_groups[idx]:
                    return "FAIL"  # City from the same group visited more than once
                visited_get = True
                visited_groups[idx] = True
                break
        if not found_group:
            return "FAIL"  # City does not belong to any group

    if not all(visited_groups):
        return "FAIL"  # Not all groups are visited

    # Requirement 3: Correct travel cost and calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not (abs(calculated_cost - total_travel_cost) < 1e-2):  # Account for floating point precision
        return "FAIL"

    # If all requirements are satisfied
    return "CORRECT"

# Cities coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Groups of cities
city_groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Given tour and cost to verify
given_tour = [0, 8, 13, 1, 14, 5, 12, 11, 0]
given_total_cost = 220.73

# Perform verification
result = verify_tour(given_tour, city_groups, cities, given_total_cost)
print(result)