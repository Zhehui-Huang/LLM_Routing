from math import sqrt

def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(tour, total_cost):
    # City coordinates
    coordinates = [
        (26, 60),  # Depot city 0
        (73, 84),  # City 1
        (89, 36),  # City 2
        (15, 0),   # City 3
        (11, 10),  # City 4
        (69, 22),  # City 5
        (28, 11),  # City 6
        (70, 2),   # City 7
        (47, 50),  # City 8
        (60, 29),  # City 9
        (29, 26),  # City 10
        (85, 68),  # City 11
        (60, 1),   # City 12
        (71, 73),  # City 13
        (82, 47),  # City 14
        (19, 25),  # City 15
        (75, 9),   # City 16
        (52, 54),  # City 17
        (64, 72),  # City 18
        (14, 89)   # City 19
    ]

    # Checks if start and end city is the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each city group is visited
    city_groups = [
        [5, 6, 16],
        [8, 18, 19],
        [11, 12, 13],
        [1, 3, 9],
        [2, 4, 14],
        [10, 17],
        [7, 15]
    ]
    visited_groups = 0
    for group in city_groups:
        if sum(1 for city in group if city in tour[1:-1]) != 1:
            return "FAIL"
        visited_groups += 1
    if visited_groups != len(city_groups):
        return "FAIL"

    # Check total calculated travel distance
    calc_total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        calc_total_cost += euclidean_distance(x1, y1, x2, y2)
    if not (abs(calc_total_cost - total_cost) < 1e-2):
        return "FAIL"

    return "CORRECT"

# Given solution details
tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]
total_cost = 266.72

# Run tests
result = verify_solution(tour, total_cost)
print(result)