import math

# Define the cities coordinates
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Provided tours for each robot
tours = [
    [0, 10, 12, 15, 11, 8, 13, 9, 14, 0],  # Robot 0
    [1, 1],                                # Robot 1
    [2, 2],                                # Robot 2
    [3, 3],                                # Robot 3
    [4, 4],                                # Robot 4
    [5, 5],                                # Robot 5
    [6, 6],                                # Robot 6
    [7, 7]                                 # Robot 7
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Check requirement 1: Each robot must start and end its tour at its assigned depot.
def check_requirement_1(tours):
    return all(tours[i][0] == i and tours[i][-1] == i for i in range(len(tours)))

# Check requirement 2: Each city must be visited exactly once by any of the robots.
def check_requirement_2(tours):
    all_visited = set(city for tour in tours for city in tour)
    return all_visited == set(range(len(cities_coordinates)))

# Compute the total travel cost of a tour
def compute_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i+1])
    return total_cjost

# Check requirement 3 and 4 implicitly by computing and assigning the total costs
def solution_correctness(tours):
    total_costs = sum(compute_travel_cost(tour) for tour in tours)
    expected_total_cost = 142.5115861601223  # As given in the solution
    return math.isclose(total_costs, expected_total_cost, abs_tol=0.01)

# Validate all requirements
def validate_solution(tours):
    if not check_requirement_1(tours):
        return "FAIL"
    if not check_requirement_2(tours):
        return "FAIL"
    if not solution_correctness(tours):
        return "FAIL"
    return "CORRECT"

# Output validation result
print(validate_solution(tours))