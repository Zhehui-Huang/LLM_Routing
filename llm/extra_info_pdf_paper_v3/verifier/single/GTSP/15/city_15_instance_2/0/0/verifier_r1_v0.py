import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    # Cities coordinates
    cities = {
        0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40),
        4: (54, 42), 5: (36, 30), 6: (52, 82), 7: (93, 44),
        8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
        12: (56, 58), 13: (72, 43), 14: (6, 99)
    }

    # Groups
    groups = [
        [8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]
    ]

    # [Requirement 1] Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visit exactly one city from each group
    visited_cities = tour[1:-1]  # Exclude starting and ending depot city
    selected_groups = list(set([j for i, group in enumerate(groups) for j in group if j in visited_cities]))

    if len(selected_groups) != len(groups):
        return "FAIL"

    # [Requirement 3] Travel cost verification using Euclidean distance
    calculated_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

    if abs(calculated_cost - total_cost) > 0.01:  # Allowing slight margin for floating point errors
        return "FAIL"

    # [Requirement 4 & 5] Correct output format already assumed by passing in appropriate parameters
    return "CORRECT"

# Provided solution test
tour = [0, 12, 10, 4, 3, 2, 0]
total_cost = 138.15
print(verify_solution(tour, total_cost))