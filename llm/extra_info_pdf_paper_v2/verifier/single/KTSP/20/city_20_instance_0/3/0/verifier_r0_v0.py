import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def test_solution():
    # Provided solution
    solution_tour = [0, 1, 8, 4, 0]
    reported_total_cost = 110.09

    # City coordinates as per problem statement
    cities = {
        0: (8, 11),
        1: (40, 6),
        2: (95, 33),
        3: (80, 60),
        4: (25, 18),
        5: (67, 23),
        6: (97, 32),
        7: (25, 71),
        8: (61, 16),
        9: (27, 91),
        10: (91, 46),
        11: (40, 87),
        12: (20, 97),
        13: (61, 25),
        14: (5, 59),
        15: (62, 88),
        16: (13, 43),
        17: (61, 28),
        18: (60, 63),
        19: (93, 15)
    }

    # Requirement 1: Visit exactly 4 cities, including the depot, starting and ending at the depot
    if len(set(solution_tour)) != 4 or solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"

    # Requirement 2 is implicitly tested by assessing the total tour length correctness

    # Requirement 3: Calculating the total travel distance
    calculated_total_distance = sum(
        calculate_euclidean_distance(cities[solution_tour[i]][0], cities[solution_tour[i]][1],
                                     cities[solution_tour[i+1]][0], cities[solution_tour[i+1]][1])
        for i in range(len(solution_tour) - 1)
    )

    # Requirement 4: Tour must start and end at depot city (city index 0)
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"

    # Check if the calculated distance matches the reported distance
    if not math.isclose(calculated_total_distance, reported_total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Run the test function and print the result
print(test_solution())