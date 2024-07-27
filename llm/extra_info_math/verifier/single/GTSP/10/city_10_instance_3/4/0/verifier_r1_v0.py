import math

# Provided city coordinates with depot city 0 always included
coordinates = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Provided groups where each inner list represents a group of city indices
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Solution derived from the solver
solution_tour = [0, 8, 8, 0]
expected_cost = 8.246211251235321

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities based on their indices """
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_requirements(tour, expected_cost):
    # [Requirement 1] Each group must be visited exactly once:
    visited = {}
    for city in tour:
        if city in coordinates:  # Ensure the city is valid
            for i, group in enumerate(groups):
                if city in group:
                    visited[i] = visited.get(i, 0) + 1
    if any(count != 1 for count in visited.values()):
        return "FAIL"

    # [Requirement 2] Must start and end at depot:
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 3] Calculate and compare the travel cost:
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(tour[i], tour[i+1])
    if abs(calculated_cost - expected_cost) > 1e-3:  # Tolerance for floating point comparison
        return "FAIL"

    return "CORRECT"

# Test the solution
test_result = check_requirements(solution_tour, expected_cost)
print(test_result)