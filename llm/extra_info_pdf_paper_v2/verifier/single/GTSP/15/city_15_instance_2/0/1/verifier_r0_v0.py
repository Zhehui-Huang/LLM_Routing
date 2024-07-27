import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Define city coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    8: (21, 78),
    11: (44, 79),
    6: (52, 82),
    2: (69, 84)
}

# Define the proposed solution tour and total cost
tour = [0, 1, 8, 11, 6, 2, 0]
reported_cost = 103.11611697272403

# City groups as per problem statement
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Testing start and end at depot
def test_tour_start_end_at_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

# Testing that exactly one city from each group is visited
def test_one_city_from_each_group(tour, groups):
    visited = tour[1:-1]  # Exclude the depot city
    unique_groups_visited = set()
    for city in visited:
        for idx, group in enumerate(groups):
            if city in group:
                unique_groups_visited.add(idx)
    return len(unique_groups_visited) == len(groups)

#Testing the tour total travel cost calculation
def test_tour_total_cost(tour, cities, reported_cost):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return math.isclose(total_cost, reported_cost, rel_tol=1e-9)

# Unit tests
def unit_tests():
    if not test_tour_start_end_at_depot(tour):
        return "FAIL"
    if not test_one_city_from_each_group(tour, groups):
        return "FAIL"
    if not test_tour_total_cost(tour, cities, reported_cost):
        return "FAIL"
    return "CORRECT"

# Output result of unit tests
print(unit_tests())