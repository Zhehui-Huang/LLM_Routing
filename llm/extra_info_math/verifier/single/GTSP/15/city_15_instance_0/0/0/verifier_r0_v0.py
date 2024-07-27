import math

# Define the positions of the cities
positions = {
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

# Define groups of the cities
groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

# Given solution
tour = [0, 8, 0, 8, 0, 0]
reported_cost = 59.84224390100319

# Function to calculate Euclidean distance
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Check if tour starts and ends at depot city 0
def check_start_end(tour):
    return tour[0] == 0 and tour[-1] == 0

# Check if tour visits exactly one city from each group
def check_groups(tour, groups):
    visited = set(tour[1:-1])  # ignore the start and end depot in validation
    for group in groups:
        if not (len(visited.intersection(group)) == 1):
            return False
    return True

# Calculate total travel cost in the tour
def calculate_total_cost(tour, positions):
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(positions[tour[i]], positions[tour[i + 1]])
    return total_cost

# Validate the tour according to the requirements
def validate_solution(tour, groups, positions, reported_cost):
    if not check_start_end(tour):
        return "FAIL"
    if not check_groups(tour, groups):
        return "FAIL"
    calculated_cost = calculate_total_cost(tour, positions)
    if not math.isclose(calculated_cost, reported_cost, abs_tol=1e-5):
        return "FAIL"
    return "CORRECT"

# Validate the given tour and reported cost
result = validate_solution(tour, groups, positions, reported_cost)
print(result)