import math

# Define cities and their coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49),
    14: (18, 49), 15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30,48)
}

# Define groups of cities
groups = [
    {7, 10, 11, 12},
    {3, 8, 13, 16},
    {2, 4, 15, 18},
    {1, 9, 14, 19},
    {5, 6, 17}
]

# Provided solution to test
tour = [0, 11, 16, 18, 19, 6, 0]
calculated_cost = 162.3829840233368

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution(tour, calculated_cost):
    # Check Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Visit exactly one city from each specified group
    groups_visited = set()
    for city in tour[1:-1]:  # Skip the depot city at start and end
        for i, group in enumerate(groups):
            if city in group:
                groups_visited.add(i)
                break
    if len(groups_visited) != len(groups):
        return "FAIL"

    # Check Requirement 3: Shortest possible path
    actual_cost = 0.0
    for i in range(len(tour) - 1):
        actual_cost += calculate_euclidean_distance(tour[i], tour[i+1])
    if not math.isclose(actual_cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Execute the test
result = test_solution(tour, calculated_cost)
print(result)