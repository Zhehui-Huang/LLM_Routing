import math

# Data input
city_positions = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}
city_groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}
provided_solution = [0, 10, 1, 9, 0]
provided_cost = 122.21527940040238

# Utility function to calculate Euclidean distance
def calculate_distance(city_a, city_b):
    x1, y1 = city_positions[city_a]
    x2, y2 = city_positions[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Check requirements
def verify_solution(path, reported_cost):
    # Check start and end at the depot
    if path[0] != 0 or path[-1] != 0:
        return "FAIL"
    
    # Check exactly one city from each group
    cities_visited = path[1:-1]  # exclude the depot occurrences
    unique_groups_visited = {g for city in cities_visited for g, cities in city_groups.items() if city in cities}
    if len(unique_groups_visited) != len(city_groups):
        return "FAIL"

    # Calculate total cost
    calculated_cost = sum(calculate_distance(path[i], path[i + 1]) for i in range(len(path) - 1))
    
    # Compare calculated cost with reported cost
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Test the provided solution
result = verify_solution(provided_solution, provided_cost)
print(result)