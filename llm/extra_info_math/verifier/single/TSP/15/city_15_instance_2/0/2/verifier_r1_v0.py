import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Coordinates of each city including the depot
city_coordinates = [
    (54, 87),  # city 0
    (21, 84),  # city 1
    (69, 84),  # city 2
    (53, 40),  # city 3
    (54, 42),  # city 4
    (36, 30),  # city 5
    (52, 82),  # city 6
    (93, 44),  # city 7
    (21, 78),  # city 8
    (68, 14),  # city 9
    (51, 28),  # city 10
    (44, 79),  # city 11
    (56, 58),  # city 12
    (72, 43),  # city 13
    (6, 99)    # city 14
]

# Tour and total travel cost given by the solver
tour = [0, 2, 7, 13, 9, 10, 5, 3, 4, 12, 8, 1, 14, 11, 6, 0]
reported_cost = 311.88

def verify_tour(tour, city_coordinates, reported_cost):
    # Check start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city except depot is visited exactly once
    visited = set(tour[1:-1])  # include cities except the return to the depot
    if len(visited) != len(city_coordinates) - 1 or any(i not in visited for i in range(1, len(city_coordinates))):
        return "FAIL"

    # Calculate the total travel cost and compare with reported cost
    calc_cost = 0
    for i in range(len(tour) - 1):
        calc_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])

    if round(calc_cost, 2) != reported_cost:
        return "FAIL"

    return "CORRECT"

# Run verification
result = verify_tour(tour, city_coordinates, reported_cost)
print(result)