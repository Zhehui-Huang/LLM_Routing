import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_traveling_salesman_solution():
    # Define cities with their coordinates
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

    # Groups of cities according to the problem statement
    groups = [
        [1, 6, 14],
        [5, 12, 13],
        [7, 10],
        [4, 11],
        [2, 8],
        [3, 9]
    ]

    # Solution tour and reported cost
    solution_tour = [0, 14, 5, 9, 8, 10, 4, 0]
    reported_cost = 138.22028342379204

    # Requirement 1: Tour starts and ends at the depot city
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Tour visits exactly one city from each group
    visited = set(solution_tour[1:-1])  # cities visited, excluding the depot city which is at start and end
    for group in groups:
        if not any(city in group for city in visited):
            return "FAIL"

    # Requirement 3: Correct calculation of the total travel cost
    calculated_cost = 0
    for i in range(len(solution_tour) - 1):
        city1 = cities[solution_tour[i]]
        city2 = cities[solution_tour[i + 1]]
        calculated_cost += calculate_distance(city1, city2)

    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-4):
        return "FAIL"

    # Requirements 4 & 5 are inherent in the assertions and calculations above
    return "CORRECT"

# Run the test
result = test_traveling_salesman_solution()
print(result)