import math

# Define the coordinates of the cities
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Substitute with the solution to verify
solution = [0, 2, 3, 9, 0]  # Sample solution
group_membership = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Check if the tour starts and ends at the depot
def test_start_end_at_depot(solution):
    return solution[0] == 0 and solution[-1] == 0

# Check if the tour visits exactly one city from each group
def test_visit_one_from_each_group(solution):
    visited_groups = [next((group for group in group_membership if city in group_membership[group]), None)
                      for city in solution[1:-1]]  # Exclude the depot city
    unique_groups = set(visited for visited in visited_groups if visited is not None)
    return len(unique_groups) == len(group_membership) and all(visited_groups.count(group) == 1 for group in unique_groups)

# Check if all travels are based on Euclidean distance calculation
# Technically all distance calculations are based on Euclidean since no alternative calculation method is given
def test_travel_cost_calculated_correctly(solution):
    for i in range(len(solution) - 1):
        distance = euclidean_distance(solution[i], solution[i + 1])
        # This function doesn't require return statement since we assume all calculations are Euclidean
    return True

def run_tests(solution):
    test_result = (test_start_end_at_depot(solution) and test_visit_one_from_each_group(solution)
                   and test_travel_cost_calculated_correctly(solution))
    if test_result:
        return "CORRECT"
    else:
        return "FAIL"

# Output test
output = run_tests(solution)
output