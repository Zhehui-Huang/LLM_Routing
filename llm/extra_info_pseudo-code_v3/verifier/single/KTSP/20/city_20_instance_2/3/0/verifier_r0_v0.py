import math

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def verify_solution(tour, total_cost, cities):
    # [Requirement 1] The solution must start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] The robot needs to visit exactly 10 cities, including the depot city
    if len(tour) != 11:  # Includes starting and ending at the depot
        return "FAIL"

    # [Requirement 5] Output the tour as a list of city indices, beginning and ending at the depot
    if not all(isinstance(city, int) for city in tour):
        return "FAIL"

    # [Requirement 6] Output the total travel cost of the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # [Requirement 3] The tour's total length (travel cost) should be calculated based on the Euclidean distance between cities
    if not math.isclose(total_cost, calculated_cost, abs_tol=1e-4):
        return "FAIL"

    # Cannot verify [Requirement 4] programmatically without the context of other possible solutions.
    # Cannot verify [Requirement 7] as it is about the method used, not the output structure.

    return "CORRECT"

# Define the coordinates of the cities
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Tour and total cost given as part of the solution
solution_tour = [0, 2, 15, 18, 7, 6, 16, 11, 19, 14, 0]
solution_total_cost = 263.6176775153687

# Check if the solution satisfies all requirements
print(verify_solution(solution_tour, solution_total_cost, cities))