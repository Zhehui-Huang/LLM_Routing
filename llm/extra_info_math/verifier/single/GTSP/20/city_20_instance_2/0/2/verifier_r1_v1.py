import math

# Define the cities and their coordinates
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

# The tour reported by the solution
reported_tour = [0, 6, 8, 3, 10, 7, 11]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Test if the tour is valid according to the requirements
def test_robot_tour(tour):
    # Requirement 2: Tour start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Identify the city groups
    visited_from_group = {
        0: [7, 10, 11, 12],
        1: [3, 8, 13, 16],
        2: [2, 4, 15, 18],
        3: [1, 9, 14, 19],
        4: [5, 6, 17]
    }
    
    # Create a mapping from city to group for checking requirement 1
    city_to_group = {city: group for group, cities in visited_from_group.items() for city in cities}
    
    # Check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the depot city (0) at the start and end
        if city in city_to_group:
            visited_groups.add(city_to_group[city])
        else:
            return "FAIL"
    
    if len(visited_group_ids) != 5:
        return "FAIL"
    
    # Requirement 3: Estimate distance and compare with reported distance
    calculated_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    reported_cost = 585.6910439829136
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Execute the test
result = test_robot_tour(reported_tour)
print(result)