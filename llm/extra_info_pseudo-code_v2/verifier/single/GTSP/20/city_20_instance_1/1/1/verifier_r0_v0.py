import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(cities_coordinates, tour, expected_cost, city_groups):
    # Check Requirement 1: Starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Visits exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the starting/ending depot city
        for group_index, group in enumerate(city_groups):
            if city in group:
                visited_groups.add(group_index)
                break
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Check Requirement 3: Calculate the travel cost using Euclidean distance
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
    if not math.isclose(cost, expected_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Given cities and their coordinates
cities_coordinates = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Groups of cities
city_groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Solution provided
tour_solution = [0, 6, 13, 2, 9, 0]
total_travel_cost_solution = 114.65928837582914

# Verification
result = verify_tour(cities_coordinates, tour_solution, total_travel_cost_solution, city_groups)
print(result)