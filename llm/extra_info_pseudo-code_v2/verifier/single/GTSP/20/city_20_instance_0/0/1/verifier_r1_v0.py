import math

# Cities and their coordinates
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

# City groups
city_groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Test the solution
def test_solution(tour, total_travel_cost):
    # Verify the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify exactly one city from each group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for group_id, group_cities in city_groups.items():
            if city in group_cities:
                visited_groups.add(group_id)
                break
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Calculate the travel cost and check it matches the given total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(tour[i], tour[i + 1])
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Given solution
solution_tour = [0, 1, 8, 4, 0]
solution_travel_cost = 110.08796524611944

# Check the solution
result = test_solution(solution_tour, solution_travel_cost)
print(result)