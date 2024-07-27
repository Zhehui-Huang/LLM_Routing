import math
from itertools import permutations

# Provided city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [
    0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15
]

# Configuration for vehicles (robots)
num_robots = 2
robot_capacity = 160

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 +
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Function to find all feasible tours given constraints
def find_feasible_tours():
    all_tours = []
    # Create all permutations of city indices, excluding depot city (0)
    for perm in permutations(range(1, len(coordinates))):
        # Build tour starting and ending at depot (0)
        tour = [0] + list(perm) + [0]
        # Check capacity constraint
        current_load = 0
        valid_tour = True
        for i in range(1, len(tour)):
            current_load += demands[tour[i]]
            if current_load > robot_capacity:
                valid_tour = False
                break
        if valid_tour:
            all_tours.append(tour)
    return all_tours

# Calculate cost for a single tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i + 1])
    return cost

# Find all feasible tours
feasible_tours = find_feasible_tours()

# Function to assign tours to robots optimally
def assign_tours_to_robots(feasible_tours):
    min_cost = float('inf')
    best_assignment = None
    # Iterate over all combinations of feasible tours for the robots
    for tours in permutations(feasible_tours, num_robots):
        total_cost = sum(calculate_tour_cost(tour) for tour in tours)
        # Check if all cities are visited exactly once by all robots combined
        all_cities = set()
        for tour in tours:
            all_cities.update(tour[1:-1])  # Exclude depot city in coverage count
        if len(all_cities) == len(coordinates) - 1 and total_cost < min_cost:
            min_cost = total_cost
            best_assignment = tours
    return best_assignment, min_cost

# Assign tours and calculate minimal cost
assigned_tours, minimum_total_cost = assign_tour