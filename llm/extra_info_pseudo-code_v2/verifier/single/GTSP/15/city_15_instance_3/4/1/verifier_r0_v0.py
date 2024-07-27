import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, expected_cost, cities, groups):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = []
    for city in tour:
        for i, group in enumerate(groups):
            if city in group:
                if i in visitedGroup_indices:
                    return "FAIL"
                visited_groups.append(i)

    if sorted(visited_groups) != list(range(len(groups))):
        return "FAIL"

    # Calculate and compare the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(total_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
          (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# City groups
groups = [[1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]]

# Provided tour and cost
tour = [0, 14, 5, 10, 11, 8, 9, 0]
expected_cost = 166.75801920718544

# Run the test
result = test_solution(tour, expected_cost, cities, groups)
print(result)