import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def check_solution(tour, total_cost):
    cities = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }

    # Check Requirement 1: The robot must start and end the tour at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Each group must be visited exactly once
    city_groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]
    visited = set(tour) - {0}  # Remove the depot's repeated entries, only unique city checks are needed
    for group in city_groups:
        if len(set(group).intersection(visited)) != 1:
            return "FAIL"  # Check if exactly one city from each group has been visited

    # Check Requirement 3: Minimize the total Euclidean distance traveled by the robot
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if abs(calculated_cost - total_cost) > 1e-5:  # Small tolerance for floating-point operations
        return "FAIL"

    return "CORRECT"

# Tour and total travel cost from the output
tour = [0, 10, 0, 10, 0, 10, 0, 10, 0]
total_travel_cost = 85.04116650187721

# Execute verification
print(check_solution(tour, total_travel_cost))