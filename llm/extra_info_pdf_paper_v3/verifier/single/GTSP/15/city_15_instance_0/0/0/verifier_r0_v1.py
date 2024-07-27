import math

# Define the coordinates of the cities
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Assume some solution for testing purposes
solution = [0, 2, 3, 9, 0]  # Example of a sample solution

# Define group membership
group_membership = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Check if the tour starts and ends at the depot
def test_start_end_at_depot(solution):
    return solution[0] == 0 and solution[-1] == 0

# Check if the solution visits exactly one city from each group
def test_visit_one_from_each_group(solution):
    visited_groups = set()
    for city in solution[1:-1]:  # Excluding the start and end depots
        for group, cities in group_membership.items():
            if city in cities:
                visited_groups.add(group)
                break
    return len(visited_groups) == len(group_membership)

# Run the tests and print the outcome
def conduct_tests(solution):
    if test_start_end_at_depot(solution) and test_visit_one_from_each_group(solution):
        return "CORRECT"
    else:
        return "FAIL"

# Output the test results
test_result = conduct_tests(solution)
print(test_result)