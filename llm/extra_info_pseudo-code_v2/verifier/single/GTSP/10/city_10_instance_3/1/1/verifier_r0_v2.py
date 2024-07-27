import unittest
from math import sqrt

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tsp_solution():
    cities = [
        (84, 67),  # depot 0
        (74, 40),  # 1
        (71, 13),  # 2
        (74, 82),  # 3
        (97, 28),  # 4
        (0, 31),   # 5
        (8, 62),   # 6
        (74, 56),  # 7
        (85, 71),  # 8
        (6, 76)    # 9
    ]
    city_groups = [
        [7, 9],
        [1, 3],
        [4, 6],
        [8],
        [5],
        [2]
    ]

    proposed_tour = [0, 7, 1, 4, 8, 5, 2, 0]
    proposed_cost = 324.18

    # Check that all cities in the tour are within the valid range
    if not all(city in range(len(cities)) for city in proposed_tour):
        return False

    # Check that the tour starts and ends at the depot
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return False

    # Calculate and check the travel cost
    total_cost_calculated = sum(euclidean_distance(cities[proposed_tour[i]], cities[proposed_tour[i + 1]])
                                for i in range(len(proposed_tour) - 1))
    if not abs(proposed_cost - total_cost_calculated) < 0.1:
        return False

    # Check each group is only visited once
    visited_groups = [False] * len(city_groups)
    for city_index in proposed_tour:
        for idx, group in enumerate(city_groups):
            if city_index in group:
                if visited_groups[idx]:
                    return False
                visited_groups[idx] = True

    if not all(visited_groups):  # Check that all groups are visited
        return False

    return True

if __name__ == "__main__":
    if check_tsp_solution():
        print("CORRECT")
    else:
        print("FAIL")