import math

# Define a function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Define the cities' coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# City groups
city_groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Provided tour solution
tour = [0, 19, 6, 2, 13, 12, 18, 0]
total_cost_reported = 158.66

# Unit Test to check all conditions:
def test_solution(tour, total_cost_reported):
    # Test if the tour starts and ends at the depot
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL: Tour does not start and end at depot."

    # Test if each group is visited exactly once
    visited_groups = []
    for city in tour[1:-1]:  # Excluding depot entries
        for i, group in enumerate(city_groups):
            if city in group:
                if i in visited_callbacks:
                    return f"FAIL: Group {i} visited more than once."
                visited_groups.append(i)
    
    if sorted(visited_groups) != list(range(len(city_groups))):
        return "FAIL: Not all groups are visited."

    # Calculate the total travel cost and compare with reported
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_cost_reported, rel_tol=1e-2):
        return f"FAIL: Total tour cost mismatch. Calculated: {calculated_cost}, Reported: {total_cost_reported}"

    return "CORRECT"

# Run the test and print the result
result = test_solution(tour, total_cost_reported)
print(result)