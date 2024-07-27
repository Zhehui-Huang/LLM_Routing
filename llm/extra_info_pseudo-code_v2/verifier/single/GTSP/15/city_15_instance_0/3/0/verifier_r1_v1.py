import math

# City coordinates corresponding to each city index
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Group information
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Create a function to calculate the Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Proposed solution tour and cost
proposed_tour = [0, 10, 1, 9, 0]
proposed_cost = 122.21527940040238

# Test function to check the validity of the proposed tour
def test_tour_and_cost(tour, cost):
    # Verify tour starts and ends at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check that each group is represented exactly once
    group_visited = {0: False, 1: False, 2: False}
    for index in tour[1:-1]:  # skip the first and last element (depot)
        for group in groups:
            if index in groups[group]:
                if group_visited[group]:
                    return "FAIL"  # group already visited
                group_visited[group] = True

    if not all(group_visited.values()):
        return "FAIL"  # Not all groups are visited
    
    # Compute total tour cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(tour[i], tour[i + 1])
    
    if not math.isclose(calculated_cost, cost, rel_tol=1e-5):
        return "FAIL"  # Calculated cost does not match the proposed cost
    
    return "CORRECT"

# Run the test function
result = test_tour_and_cost(proposed_tour, proposed_cost)
print(result)