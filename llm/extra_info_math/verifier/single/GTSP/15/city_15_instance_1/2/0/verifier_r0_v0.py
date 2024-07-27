import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost):
    city_coordinates = {
        0: (29, 51),
        1: (49, 20),
        2: (79, 69),
        3: (17, 20),
        4: (18, 61),
        5: (40, 57),
        6: (57, 30),
        7: (36, 12),
        8: (93, 43),
        9: (17, 36),
        10: (4, 60),
        11: (78, 82),
        12: (83, 96),
        13: (60, 50),
        14: (98, 1)
    }
    city_groups = [
        {1, 2, 5, 6},
        {8, 9, 10, 13},
        {3, 4, 7},
        {11, 12, 14}
    ]

    # Checking start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Checking visitation of one city from each group
    visited_groups = [set() for _ in range(4)]
    for index, city_index in enumerate(tour[1:-1]):  # exclude depot city at start and end
        for group_index, group in enumerate(city_groups):
            if city_index in group:
                visited_groups[group_index].add(city_index)

    if any(len(group) != 1 for group in visited_groups):
        return "FAIL"

    # Checking travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # Comparing given and calculated cost with some tolerance to handle floating point arithmetic issues
    if not math.isclose(total_travel_cost, calculated_cost, abs_tol=0.001):
        return "FAIL"

    return "CORRECT"

# Test the solution
tour = [0, 4, 0]
total_travel_cost = 29.732137494637012
print(verify_solution(tour, total_travel_cost))