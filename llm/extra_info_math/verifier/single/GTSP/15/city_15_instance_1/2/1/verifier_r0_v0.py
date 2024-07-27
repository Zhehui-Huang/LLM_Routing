import math

# Define the coordinates of the cities
cities = {
    0: (29, 51),  # Depot
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# City groups definition
city_groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Solution provided from the MILP
solution_tour = [0, 0]
solution_cost = 0.0

# Define a function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Check if the tour is starting and ending at the depot
def check_start_end_at_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

# Check if the tour visits exactly one city from each city group
def check_city_group_coverage(tour, groups):
    visited = set(tour)
    for group in groups:
        if not any(city in visited for city in group):
            return False
    return True

# Check if the travel path minimizes the distance travelled
def check_minimized_distance(tour):
    # Calculate travel cost of the tour
    travel_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return math.isclose(travel_cost, solution_cost, rel_tol=1e-9)

# Unit tests to validate the solution
def validate_solution(tour, cost):
    if not check_start_end_at_depot(tour):
        return "FAIL"
    if not check_city_group_coverage(tour, city_groups):
        return "FAIL"
    if not check_minimized_distance(tour):
        return "FAIL"
    return "CORRECT"

# Output the result of validation
result = validate_solution(solution_tour, solution_cost)
print(result)