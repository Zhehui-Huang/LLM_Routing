import math

# Given data
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}
city_groups = {
    0: [3, 8], 1: [4, 13], 2: [1, 2], 3: [6, 14],
    4: [5, 9], 5: [7, 12], 6: [10, 11]
}

# Solution provided
tour = [0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 0]
reported_cost = 148.82

def calculate_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_requirements(tour, reported_cost):
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit exactly one city from each city group
    visited_cities_from_groups = set()
    for city in tour:
        for group_id, cities in city_groups.items():
            if city in cities:
                if group_id in visited_cities_from_groups:
                    return "FAIL"
                visited_cities_from_groups.add(group_id)
    if len(visited_cities_from_groups) != len(city_groups):
        return "FAIL"

    # Check if the tour respects the problem constraints 
    for i in range(len(tour) - 1):
        if tour[i] == tour[i + 1] and tour[i] != 0:
            return "FAIL"

    # Requirement 3: Check the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Evaluate the solution and return the result
result = verify_requirements(tour, reported_cost)
print(result)