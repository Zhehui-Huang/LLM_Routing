import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, expected_cost):
    cities = {
        0: (35, 40),
        1: (39, 41),
        2: (81, 30),
        3: (5, 50),
        4: (72, 90),
        5: (54, 46),
        6: (8, 70),
        7: (97, 62),
        8: (14, 41),
        9: (70, 44),
        10: (27, 47),
        11: (41, 74),
        12: (53, 80),
        13: (21, 21),
        14: (12, 39)
    }

    city_groups = [
        [3, 8],
        [4, 13],
        [1, 2],
        [6, 14],
        [5, 9],
        [7, 12],
        [10, 11]
    ]

    # Verify Requirement 1: Tour starts and ends at the depot city
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Verify Requirement 2: The robot must visit exactly one city from each of the 7 defined city groups
    unique_visited = set()
    visited_groups = set()
    for city in tour:
        if city in unique_visited and city != 0:
            return "FAIL"
        unique_visited.add(city)
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups.add(i)
                break

    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Verify Requirement 3 and Requirement 5: Calculate and verify total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Requirement 4 & 6 are based on output structure and optimization efforts; cannot be tested without comparison to all possible solutions
    
    return "CORRECT"

# Provided solution
tour_solution = [0, 1, 5, 7, 4, 6, 3, 10, 0]
cost_solution = 223.461137669551

result = verify_solution(tour_solution, cost_solution)
print(result)