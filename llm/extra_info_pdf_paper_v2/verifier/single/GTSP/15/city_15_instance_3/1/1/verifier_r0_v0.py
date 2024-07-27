import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, total_cost):
    cities = {
        0: (16, 90),
        1: (43, 99),
        2: (80, 21),
        3: (86, 92),
        4: (54, 93),
        5: (34, 73),
        6: (6, 61),
        7: (86, 69),
        8: (30, 50),
        9: (35, 73),
        10: (42, 64),
        11: (64, 30),
        12: (70, 95),
        13: (29, 64),
        14: (32, 79)
    }
    groups = [
        [1, 6, 14],
        [5, 12, 13],
        [7, 10],
        [4, 11],
        [2, 8],
        [3, 9]
    ]

    # Check starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if it visits exactly one city from each group
    visited_groups = [False] * len(groups)
    for city in tour[1:-1]:  # Ignoring the first and last city (depot)
        for index, group in enumerate(groups):
            if city in group:
                if visited_groups[index]:
                    return "FAIL"
                visited_groups[index] = True
                break
    if not all(visited_groups):
        return "FAIL"

    # Check total travel cost
    computed_cost = 0
    for idx in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[idx]], cities[tour[idx + 1]])

    if not math.isclose(computed_cost, total_cost, rel_tol=1e-02):  # Allowing small floating point tolerance
        return "FAIL"

    return "CORRECT"

# Tour and cost from the provided solution
tour = [0, 14, 5, 10, 11, 8, 9, 0]
total_cost = 166.76

# Check if the solution meets the requirements
result = verify_tour(tour, total_cost)
print(result)